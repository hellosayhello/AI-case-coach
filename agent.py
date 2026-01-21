import os
import asyncio
import json
from dotenv import load_dotenv

from livekit import agents, rtc
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    cli,
    llm,
)

import sys
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

def log(msg):
    print(msg, flush=True)
    with open("/tmp/agent_debug.log", "a") as f:
        f.write(msg + "\n")

log("=== AGENT.PY STARTING ===")

from livekit.plugins import openai, silero
from cases import CASE_LIBRARY 

load_dotenv()

server = AgentServer()

# --- GRAPH DISPLAY LOGIC ---
async def show_graph(room, graph_config):
    """Send a graph to the frontend for display."""
    print(f"--- SHOWING GRAPH: {graph_config['image_url']} ---")
    
    payload = json.dumps({
        "type": "SHOW_GRAPH",
        "image_url": graph_config["image_url"],
        "display_prompt": graph_config.get("display_prompt", "Please analyze this chart."),
    })
    
    await room.local_participant.publish_data(
        payload=payload.encode("utf-8"),
        topic="feedback",
        reliable=True
    )

# --- GRADING LOGIC ---
async def generate_feedback(formatted_history, llm_instance):
    print("--- GENERATING FEEDBACK ---", flush=True)
    system_prompt = """
    You are a senior BCG interviewer grading a candidate. 
    Review the transcript below.
    CRITICAL: Check if their verbal math matches the correct answers
    
    SCORING GUIDELINES:
    - 9-10: Excellent performance, minor or no issues
    - 7-8: Good performance, met expectations with small areas for improvement
    - 5-6: Average performance, some gaps but acceptable
    - 3-4: Below expectations, significant issues
    - 1-2: Poor performance, major problems
    
    Be generous but fair. If the candidate demonstrated good structure, correct math, 
    and clear communication, scores should be 7-9. Only give low scores (below 5) 
    for significant mistakes or missing key elements.
    
    Return ONLY a JSON object:
    {
      "score": 0,
      "feedback_text": "Summary...",
      "buckets": {
        "Structured Thinking": {"score": 0, "comment": "..."},
        "Data Processing": {"score": 0, "comment": "..."},
        "Communications": {"score": 0, "comment": "..."},
        "Creativity": {"score": 0, "comment": "..."}
      }
    }
    """
    
    # Use OpenAI directly
    from openai import AsyncOpenAI
    client = AsyncOpenAI()
    
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"TRANSCRIPT:\n{formatted_history}"}
        ]
    )
    
    full_response = response.choices[0].message.content
    log(f"--- FEEDBACK GENERATED ---")
    log(f"    Response: {full_response[:200]}...")
    
    return full_response.replace("```json", "").replace("```", "").strip()

async def run_grading_task(history_text, room):
    log("--- STARTING GRADING TASK ---")
    log(f"    History length: {len(history_text)} chars")
    
    try:
        # Notify Frontend
        await room.local_participant.publish_data(
            payload=json.dumps({"type": "STATUS", "msg": "Analyzing..."}), 
            topic="feedback",
            reliable=True
        )
        log("--- STATUS SENT TO FRONTEND ---")
        
        # Run Grading
        grading_llm = openai.LLM(model="gpt-4o") 
        feedback_json = await generate_feedback(history_text, grading_llm)
        log(f"--- FEEDBACK GENERATED ---")
        log(f"    Response: {feedback_json[:300]}...")
        
        # Send Result
        await room.local_participant.publish_data(
            payload=feedback_json.encode("utf-8"), 
            topic="feedback",
            reliable=True
        )
        log("--- FEEDBACK SENT TO FRONTEND ---")
        
    except Exception as e:
        log(f"--- ERROR IN GRADING TASK: {e} ---")
        import traceback
        traceback.print_exc()
        
# --- MAIN ENTRYPOINT ---
@server.rtc_session()
async def entrypoint(ctx: JobContext):
    await ctx.connect()
    participant = await ctx.wait_for_participant()
    
    selected_case_id = "phighting_phillies"
    if participant.metadata:
        try:
            meta = json.loads(participant.metadata)
            selected_case_id = meta.get("selectedCase", "phighting_phillies")
        except: pass

    case_data = CASE_LIBRARY.get(selected_case_id, CASE_LIBRARY["phighting_phillies"])
    print(f"--- LOADING CASE: {case_data['title']} ---")

    # Track which graphs have been shown
    shown_graphs = set()

    # Build exhibit info for the LLM
    exhibit_info = ""
    graphs = case_data.get("graphs", {})
    if graphs:
        exhibit_info = """
    --- EXHIBIT DISPLAY PROTOCOL ---
    This case has visual exhibits shown to the candidate automatically.
    
    AVAILABLE EXHIBITS:
"""
        for key, config in graphs.items():
            exhibit_info += f'    - To show "{key}": Say exactly "{config.get("trigger_phrase")}"\n'
        
        exhibit_info += """
    RULES:
    1. Say the trigger phrase EXACTLY as written when ready to show an exhibit
    2. After saying it, pause and ask "What do you observe?"
    3. Let the candidate interpret before providing specific numbers
"""

    dynamic_instructions = f"""
    ROLE: You are Brian, a BCG Manager. 
    You are interviewing a candidate for an Associate position. 
    Your personality is professional, slightly challenging, but fair.
    
    --- CASE CONTEXT ---
    TITLE: {case_data['title']}
    INDUSTRY: {case_data.get('industry', 'General')}
    CONTEXT: {case_data['prompt']['context']}
    OBJECTIVE: {case_data.get('prompt', {}).get('objectives', case_data['prompt'].get('objective'))}

    {exhibit_info}

    --- THE PASSIVE INTERVIEWER PROTOCOL ---
    0. THE "READY" TRAP: 
       - IF the user says "I am ready to present", "I have my structure", or "Here is my plan" BUT does not list specific buckets:
       - SAY ONLY: "Please walk me through it." or "Go ahead."
    1. NEVER LEAD THE WITNESS: Do not suggest the next step.
    2. FORCE THE DRIVE: If the candidate stops talking, wait.
    3. DATA GATING: Never volunteer data. Only provide if asked.
    4. CONVERSATIONAL LISTS: Do not use numbered lists.

    --- PHASE 1: FRAMEWORK & STRUCTURE ---
    - Start by introducing the case context and objective.
    - Ask the candidate to structure their approach.
    - CLARIFYING DATA: {json.dumps(case_data.get('clarifying_info', {}))}

    --- PHASE 2: ANALYSIS & DATA ---
    - Guide the candidate through the analysis. 
    - ANSWER KEY (FOR YOUR EYES ONLY): 
    {json.dumps({k: case_data[k] for k in ["financial_data", "market_sizing", "math_benchmarks", "scenario_math", "synergy_potential", "profitability", "grocery_impact", "economics", "phase_1_brainstorming", "phase_3_math"] if k in case_data}, indent=2)}

    *** CRITICAL DATA SHARING RULES ***
    1. SHARE INPUTS ONLY: Provide ONLY raw variables if asked.
    2. WITHHOLD OUTPUTS: NEVER reveal calculated figures unless confirming.
    3. IF ASKED FOR ANSWER: Ask "How would you calculate it?"

    --- PHASE 3: RECOMMENDATION & CLOSING ---
    - Ask for a final recommendation. 
    - Once the candidate gives their recommendation, acknowledge it briefly.
    - THEN, SAY EXACTLY THIS: "This concludes the case. If you are ready to see your performance report, just say 'I want to review my case feedback'."
    - Wait for them to say it.
    
    --- INTERVIEWER GUIDANCE ---
    {json.dumps(case_data.get('interviewer_guide', ''), indent=2)}
    """

    session = AgentSession(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"), 
        tts=openai.TTS(),
        min_endpointing_delay=0.5
    )
    
    # LISTEN FOR USER INPUT
    @session.on("user_input_transcribed")
    def on_user_input(event):
        text = event.transcript.lower()
        
        # Thinking Delay Logic
        if any(p in text for p in ["minute to structure", "take some time", "thinking"]):
            session.min_endpointing_delay = 300.0
            print("--- 300s DELAY ---")
        elif any(p in text for p in ["ready", "framework", "finished", "go ahead"]):
            session.min_endpointing_delay = 0.5
            print("--- DELAY RESET ---")
            
        # TRIGGER FEEDBACK ON VOICE COMMAND
        if "review my case feedback" in text or "review my feedback" in text:
            print(f"--- DETECTED MAGIC WORD: {text} ---")
            history = agent.chat_ctx.items
            formatted = "\n".join([f"{m.role}: {m.content}" for m in history])
            asyncio.create_task(run_grading_task(formatted, ctx.room))

    # LISTEN FOR AGENT SPEECH - Trigger graph on exact phrase match
    @session.on("conversation_item_added")
    def on_conversation_item(event):
        print(f">>> CONVERSATION ITEM ADDED <<<")
        print(f"    Event: {event}")
        print(f"    Item: {event.item}")
        
        # Check if it's an agent message
        item = event.item
        if hasattr(item, 'role') and item.role == 'assistant':
            agent_text = ""
            if hasattr(item, 'content'):
                agent_text = str(item.content).lower()
            elif hasattr(item, 'text'):
                agent_text = item.text.lower()
            
            print(f"    Agent text: {agent_text[:100] if agent_text else 'empty'}...")
            
            # Check for trigger phrase
            graphs = case_data.get("graphs", {})
            for graph_key, graph_config in graphs.items():
                if graph_key in shown_graphs:
                    continue
                
                trigger_phrase = graph_config.get("trigger_phrase", "")
                if trigger_phrase and trigger_phrase in agent_text:
                    shown_graphs.add(graph_key)
                    asyncio.create_task(show_graph(ctx.room, graph_config))
                    print(f"--- GRAPH TRIGGERED: {graph_key} ---")
                    return

    agent = Agent(instructions=dynamic_instructions)
    await session.start(agent=agent, room=ctx.room)

    await asyncio.sleep(1.0)
    
    greeting_text = f"Hi, I'm Brian. I am your interviewer today and I look forward to our case discussion. Diving into the case, {case_data['prompt']['context']}The client wants us to {case_data['prompt']['objective']}"
    await session.generate_reply(instructions=f"Say exactly this: '{greeting_text}'")

if __name__ == "__main__":
    cli.run_app(server)
