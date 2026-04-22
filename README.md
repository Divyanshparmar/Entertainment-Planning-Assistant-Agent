# Entertainment-Planning-Assistant-Agent

🎬 Planner Agent for Entertainment Tasks
📌 Overview

The Planner Agent is an intelligent system designed to orchestrate complex entertainment-related tasks using a multi-step reasoning loop. Given a high-level goal (e.g., “Analyze popular movies” or “Generate movie reviews”), the agent autonomously:

Breaks down the goal into smaller actionable tasks
Validates resource availability using mock tools
Plans execution order with dependency handling
Generates a structured execution workflow

This project demonstrates how AI agents can think, plan, and act step-by-step, rather than generating direct outputs.

🚀 Features
🧠 Multi-Step Reasoning Loop
Iteratively plans → evaluates → refines tasks
🧩 Task Decomposition
Converts high-level goals into smaller subtasks
🔗 Dependency Management
Ensures tasks are executed in the correct order
🛠️ Tool Validation (Mock Interfaces)
Simulates availability of APIs, data sources, or services
📅 Execution Scheduling
Generates a structured plan with step-by-step execution
🔄 Dynamic Adaptability
Adjusts plan based on constraints or missing resources
🏗️ Architecture
User Goal
   ↓
Planner Agent
   ↓
Task Decomposition
   ↓
Dependency Analysis
   ↓
Tool Validation
   ↓
Execution Plan Generation
⚙️ Tech Stack
Python
Streamlit (for UI)
Ollama (LLM) (e.g., TinyLlama / other models)
Requests (API communication)
📂 Project Structure
project/
│── app.py                  # Streamlit UI
│── agent/
│   ├── __init__.py
│   ├── planner.py          # Core Planner Agent logic
│   ├── tools.py            # Mock tools for validation
│── utils/
│   ├── helpers.py
│── requirements.txt
│── README.md
🔄 How It Works
1. Input Goal

User provides a high-level objective:

"Analyze popular movies"
2. Task Decomposition

Agent breaks it into:

Fetch popular movies
Extract metadata
Perform sentiment analysis
Generate summary
3. Tool Validation

Agent checks:

Internet access ✅
API availability ✅
Data source ❌ (fallback triggered)
4. Execution Planning

Final structured plan:

Step 1: Fetch movie list  
Step 2: Collect reviews  
Step 3: Analyze sentiment  
Step 4: Generate insights  
▶️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/planner-agent.git
cd planner-agent
2. Install Dependencies
pip install -r requirements.txt
3. Run Ollama (if using local LLM)
ollama run tinyllama
4. Run Streamlit App
streamlit run app.py
🧪 Example Usage
Input:
Generate movie reviews
Output:
Task breakdown
Tool validation report
Step-by-step execution plan

⚠️ Note: This agent generates a plan, not the final content output.

🎯 Use Cases
🎥 Movie analysis & review planning
📺 Content recommendation workflows
🧠 AI agent research & experimentation
📊 Task orchestration systems
🔮 Future Improvements
✅ Integrate real APIs (IMDb, TMDb)
🤖 Replace mock tools with real services
🧾 Generate final outputs (not just plans)
🔄 Add feedback loop for plan refinement
🌐 Deploy as a web service
