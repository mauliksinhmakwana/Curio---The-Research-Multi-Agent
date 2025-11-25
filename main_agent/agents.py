from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import operator

# --- 1. Setup the Brain (Gemini) ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# --- 2. Define the State (Memory) ---
# This acts as the "Memory Bank" passed between agents
class AgentState(TypedDict):
    topic: str
    plan: List[str]
    research_notes: List[str]
    final_report: str

# --- 3. Define the Agents ---

def guide_agent(state: AgentState):
    """The Planner: Breaks the topic into 3 steps."""
    print("🗺️  Guide is planning the journey...")
    topic = state['topic']
    
    prompt = f"""
    You are 'The Guide', a helpful project planner.
    User wants to know about: {topic}.
    Break this down into 3 distinct, simple search queries to get a full picture.
    Return ONLY the 3 queries separated by newlines. No other text.
    """
    response = llm.invoke(prompt)
    plan = response.content.strip().split('\n')
    return {"plan": plan}

def scout_agent(state: AgentState):
    """The Researcher: Loops through the plan and searches."""
    from tools import web_search # Import here to avoid circular imports
    
    plan = state['plan']
    notes = []
    
    print("🔭 Scout is gathering information...")
    
    # Loop Pattern (Iterating through the plan)
    for query in plan:
        # Using the Tool
        search_result = web_search.invoke(query)
        # Context Engineering (Summarizing the raw search to save tokens)
        summary_prompt = f"Summarize this search result in 2 bullet points: {search_result}"
        summary = llm.invoke(summary_prompt).content
        notes.append(f"Query: {query}\nFindings: {summary}")
        
    return {"research_notes": notes}

def scribe_agent(state: AgentState):
    """The Writer: Compiles the final friendly report."""
    print("✍️  Scribe is writing the story...")
    topic = state['topic']
    notes = "\n\n".join(state['research_notes'])
    
    prompt = f"""
    You are 'The Scribe', a warm and engaging writer.
    Topic: {topic}
    Research Notes: {notes}
    
    Write a comprehensive but easy-to-read blog post in Markdown format.
    Use emojis, clear headings, and a friendly tone.
    """
    response = llm.invoke(prompt)
    return {"final_report": response.content}

# --- 4. Build the Graph (Orchestration) ---
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("guide", guide_agent)
workflow.add_node("scout", scout_agent)
workflow.add_node("scribe", scribe_agent)

# Add Edges (The Flow)
workflow.set_entry_point("guide")
workflow.add_edge("guide", "scout")
workflow.add_edge("scout", "scribe")
workflow.add_edge("scribe", END)

# Compile
app = workflow.compile()
