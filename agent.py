import os
import asyncio
import json
from dotenv import load_dotenv

# --- IMPORTS (Standard Agent Only) ---
from livekit import agents, rtc
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    cli,
    llm,
)
from livekit.plugins import openai, silero
from cases import CASE_LIBRARY 

load_dotenv()

server = AgentServer()

# --- GRADING LOGIC ---
async def generate_feedback(formatted_history, llm_instance):
    print("--- GENERATING FEEDBACK ---")
    system_prompt = """
    You are a senior BCG interviewer grading a candidate. 
    Review the transcript below.
    CRITICAL: Check if their verbal math matches the correct answers ($300M Revenue, $1B Valuation, etc).
    
    Return ONLY a JSON object:
    {
      "score": 0,
      "feedback_text": "Summary...",
      "buckets": {
        "Structure": {"score": 0, "comment": "..."},
        "Data & Math": {"score": 0, "comment": "..."},
        "Communication": {"score": 0, "comment": "..."},
        "Creativity": {"score": 0, "comment": "..."}
      }
    }
    """
    chat_ctx = llm.ChatContext().append(role="system", text=system_prompt)
    chat_ctx.append(role="user", text=f"TRANSCRIPT:\n{formatted_history}")
    stream = llm_instance.chat(chat_ctx=chat_ctx)
    full_response = ""
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
    return full_response.replace("```json", "").replace("```", "").strip()

async def run_grading_task(history_text, room):
    # Notify Frontend
    await room.local_participant.publish_data(
        payload=json.dumps({"type": "STATUS", "msg": "Analyzing..."}), 
        topic="feedback",
        reliable=True
    )
    # Run Grading
    grading_llm = openai.LLM(model="gpt-4o") 
    feedback_json = await generate_feedback(history_text, grading_llm)
    # Send Result
    await room.local_participant.publish_data(
        payload=feedback_json.encode("utf-8"), 
        topic="feedback",
        reliable=True
    )

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

    dynamic_instructions = f"""
    ROLE: You are Brian, a BCG Manager. 
    You are interviewing a candidate for an Associate position. 
    Your personality is professional, slightly challenging, but fair.
    
    --- CASE CONTEXT ---
    TITLE: {case_data['title']}
    INDUSTRY: {case_data.get('industry', 'General')}
    CONTEXT: {case_data['prompt']['context']}
    OBJECTIVE: {case_data.get('prompt', {}).get('objectives', case_data['prompt'].get('objective'))}

    --- THE PASSIVE INTERVIEWER PROTOCOL ---
    0. THE "READY" TRAP: 
       - IF the user says "I am ready to present", "I have my structure", or "Here is my plan" BUT does not list specific buckets:
       - SAY ONLY: "Please walk me through it." or "Go ahead."
    1. NEVER LEAD THE WITNESS: Do not suggest the next step.
    2. FORCE THE DRIVE: If the candidate stops talking, wait.
    3. DATA GATING: Never volunteer data. Only provide if asked.
    4. CONVERSATIONAL LISTS: Do not use numbered lists.

    --- PHASE 1: FRAMEWORK & STRUCTURE ---
    - Start by introducing the case context.
    - Ask the candidate to structure their approach.
    - CLARIFYING DATA: {json.dumps(case_data.get('clarifying_info', {}))}

    --- PHASE 2: ANALYSIS & DATA ---
    - Guide the candidate through the analysis. 
    - ANSWER KEY (FOR YOUR EYES ONLY): 
    {json.dumps(relevant_analysis_data := {k: case_data[k] for k in ["financial_data", "market_sizing", "math_benchmarks", "scenario_math", "synergy_potential", "profitability", "grocery_impact", "economics", "phase_1_brainstorming", "phase_3_math"] if k in case_data}, indent=2)}

    *** CRITICAL DATA SHARING RULES ***
    1. SHARE INPUTS ONLY: Provide ONLY raw variables if asked.
    2. WITHHOLD OUTPUTS: NEVER reveal calculated figures (Total Revenue, Profit) unless confirming.
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
    
    # LISTEN FOR MAGIC WORD
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
            history = agent.chat_ctx.messages
            formatted = "\n".join([f"{m.role}: {m.content}" for m in history])
            asyncio.create_task(run_grading_task(formatted, ctx.room))

    agent = Agent(instructions=dynamic_instructions)
    await session.start(agent=agent, room=ctx.room)

    # Small delay for audio connection
    await asyncio.sleep(1.0)
    
    greeting_text = f"Hi, I'm Brian. I am your interviewer today and I look forward to our case discussion. Diving into the case, {case_data['prompt']['context']}"
    await session.generate_reply(instructions=f"Say exactly this: '{greeting_text}'")

if __name__ == "__main__":
    cli.run_app(server)
