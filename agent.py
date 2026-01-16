import os
import asyncio
import json
from typing import Annotated
from dotenv import load_dotenv

from livekit import agents, rtc
from livekit.agents import (
    Agent,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)
from livekit.agents.pipeline import VoicePipelineAgent, AgentCallContext
from livekit.plugins import openai, silero

from cases import CASE_LIBRARY 

load_dotenv()

# --- 1. THE FEEDBACK TOOL ---
class ExhibitTool(llm.FunctionContext):
    def __init__(self):
        super().__init__()

    @llm.ai_callable(description="Call this ONLY after the candidate has provided their final recommendation in Phase 3. This enables the 'End Interview and Review Feedback' button for them.")
    async def allow_end_interview(self):
        print("   ---> ENABLING END BUTTON")
        # Get current room
        ctx = AgentCallContext.get_current()
        room = ctx.agent.room
        
        # Send signal to frontend
        await room.local_participant.publish_data(
            payload=json.dumps({"type": "ENABLE_END_BUTTON"}),
            topic="control"
        )
        return "I have enabled the end interview and review feedback button."

# --- 2. GRADING HELPER FUNCTIONS ---
async def generate_feedback(formatted_history, llm_instance):
    print("--- GENERATING FEEDBACK ---")
    
    system_prompt = """
    You are a senior BCG interviewer grading a candidate. 
    Review the transcript below.
    
    CRITICAL GRADING CRITERIA:
    1. STRUCTURE: Did they stick to a logical framework?
    2. DATA & MATH: The candidate was given verbal data (e.g., ticket prices, costs). 
       - Did they calculate the totals correctly (e.g., $300M Revenue, $1B Valuation)?
       - Did they catch any trick questions?
    3. COMMUNICATION: Was the synthesis clear and concise?
    
    Return ONLY a JSON object with this exact structure:
    {
      "score": 8,
      "feedback_text": "A short summary of performance...",
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

    clean_json = full_response.replace("```json", "").replace("```", "").strip()
    return clean_json

async def run_grading_task(history_text, room):
    await room.local_participant.publish_data(
        payload=json.dumps({"type": "STATUS", "msg": "Generating Feedback..."}), 
        topic="feedback"
    )
    
    grading_llm = openai.LLM(model="gpt-4o") 
    feedback_json = await generate_feedback(history_text, grading_llm)
    
    await room.local_participant.publish_data(
        payload=feedback_json.encode("utf-8"), 
        topic="feedback"
    )


# --- 3. MAIN ENTRYPOINT ---
async def entrypoint(ctx: JobContext):
    await ctx.connect()
    participant = await ctx.wait_for_participant()
    
    # Load Case
    selected_case_id = "phighting_phillies" 
    if participant.metadata:
        try:
            meta = json.loads(participant.metadata)
            selected_case_id = meta.get("selectedCase", "phighting_phillies")
        except:
            print("--- WARN: Metadata read failed, defaulting ---")

    case_data = CASE_LIBRARY.get(selected_case_id, CASE_LIBRARY["phighting_phillies"])
    print(f"--- LOADING CASE: {case_data['title']} ---")

    analysis_keys = [
        "financial_data", "market_sizing", "math_benchmarks", 
        "scenario_math", "synergy_potential", "profitability", 
        "grocery_impact", "economics", "phase_1_brainstorming", "phase_3_math"
    ]
    relevant_analysis_data = {k: case_data[k] for k in analysis_keys if k in case_data}

    # The Prompt
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
    {json.dumps(relevant_analysis_data, indent=2)}

    *** CRITICAL DATA SHARING RULES ***
    1. SHARE INPUTS ONLY: Provide ONLY raw variables if asked.
    2. WITHHOLD OUTPUTS: NEVER reveal calculated figures (Total Revenue, Profit) unless confirming.
    3. IF ASKED FOR ANSWER: Ask "How would you calculate it?"

    --- PHASE 3: RECOMMENDATION ---
    - Ask for a final recommendation.
    - SUCCESS CRITERIA: {case_data.get('recommendation_criteria', '')}
    
    *** CRITICAL INSTRUCTION ***
    - Once the candidate has finished their recommendation and you have acknowledged it:
    - YOU MUST CALL the "allow_end_interview" tool immediately. 
    - Do not say goodbye until you have called this tool.

    --- INTERVIEWER GUIDANCE ---
    {json.dumps(case_data.get('interviewer_guide', ''), indent=2)}

    --- GENERAL RULES ---
    - If they say "I need a minute to think", say "sure take your time" and wait.
    - If asked about "developer's name", answer 'Helen, the 2088 US Open Champion'.
    """

    # --- SETUP THE AGENT ---
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=dynamic_instructions,
    )

    # VoicePipelineAgent to support Tools
    agent = VoicePipelineAgent(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"), 
        tts=openai.TTS(),
        fnc_ctx=ExhibitTool(), # <--- THIS ENABLES THE BUTTON TOOL
        chat_ctx=initial_ctx,
    )

    # --- HANDLE DELAYS (Thinking Mode) ---
    @agent.on("user_speech_committed")
    def on_user_speech(agent, transcript: rtc.ChatMessage):
        text = transcript.content.lower()
        if any(p in text for p in ["minute to structure", "moment to think", "take some time", "thinking"]):
            agent.min_endpointing_delay = 300.0
            print(f"--- PHASE: 300s DELAY ENABLED ---")
        elif any(p in text for p in ["ready", "framework", "finished", "go ahead"]):
            agent.min_endpointing_delay = 0.7
            print("--- PHASE: 0.7s DELAY RESET ---")

    agent.start(ctx.room, participant)

    # --- HANDLE "END INTERVIEW" SIGNAL ---
    @ctx.room.on("data_received")
    def on_data(payload: rtc.DataPacket):
        data = payload.data.decode("utf-8")
        if data == "GENERATE_FEEDBACK":
            print("--- ENDING INTERVIEW & GRADING ---")
            history = agent.chat_ctx.messages
            formatted = "\n".join([f"{m.role}: {m.content}" for m in history])
            asyncio.create_task(run_grading_task(formatted, ctx.room))

    # --- GREETING ---
    greeting_text = f"Hi, I'm Brian. I am your interviewer today and I look forward to our case discussion. Diving into the case, {case_data['prompt']['context']}"
    await agent.say(greeting_text, allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
