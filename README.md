# 🌟 Curio: The Empathetic Research Companion

Curio is a multi-agent system designed to make complex research feel like a conversation with a smart friend. Instead of overwhelming you with data, Curio employs a team of specialized AI agents to plan, research, and narrate a story around your topic of interest.

## Features

### 1. 🤖 Multi-Agent Architecture
Curio operates using a sequential **Supervisor-Worker** flow:
* **The Guide (Planner):** Uses LLM reasoning to decompose a user query into a strategic 3-step research plan.
* **The Scout (Researcher):** Executes a **Loop** pattern, iterating through the plan and using external tools to gather "grounded" facts.
* **The Scribe (Writer):** Synthesizes disjointed facts into a cohesive, human-friendly narrative.

### 2. Tools & Interoperability
* **DuckDuckGo Search:** Used by the 'Scout' agent to fetch real-time, real-world data (Grounding).
* **File System Tool:** Used to persist the final output into a Markdown file.

### 3. Context & Memory
* **State Management:** Built on `LangGraph`, Curio uses a shared `AgentState` (Memory Bank) to pass context (plans, raw notes, summaries) between agents without losing information.
* **Context Engineering:** The Scout agent summarizes raw search data *before* passing it to the Scribe, optimizing context window usage (Context Compaction).

### 4. Observability
* The system includes console-based logging (traces) that show the user exactly which agent is working and what they are "thinking" in real-time.

## What I Learned
Through building Curio, I learned that **Agent Orchestration** is more powerful than a single zero-shot prompt. By separating "Planning" from "Execution," the system avoids getting distracted and produces significantly higher-quality research.

---
*Created with ❤️*
