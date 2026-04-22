import json
import requests
import re


# ===============================
# 🔹 CALL OLLAMA
# ===============================
def call_ollama(prompt, model="qwen2.5:3b"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            },
            timeout=60
        )
        return response.json().get("response", "")
    except Exception as e:
        print("⚠️ Ollama API Error:", e)
        return ""


# ===============================
# 🔹 ALLOWED TASKS
# ===============================
ALLOWED_TASKS = [
    "Fetch movies",
    "Get ratings",
    "Analyze reviews",
    "Generate summary",
    "Select event",
    "Book venue",
    "Send invitations",
    "Finalize schedule"
]


# ===============================
# 🔹 FALLBACK ENGINE
# ===============================
def fallback_logic(goal):
    goal = goal.lower()

    if any(w in goal for w in ["movie", "film", "cinema"]):
        return [
            "Fetch movies",
            "Get ratings",
            "Analyze reviews",
            "Generate summary"
        ]

    if any(w in goal for w in ["event", "party", "function"]):
        return [
            "Select event",
            "Book venue",
            "Send invitations",
            "Finalize schedule"
        ]

    return ["Unknown Goal"]


# ===============================
# 🔹 SAFE JSON PARSER
# ===============================
def parse_model_output(output):
    try:
        # Try direct JSON
        data = json.loads(output)
        if isinstance(data, list):
            return data
    except:
        pass

    # Try extracting JSON from messy output
    match = re.search(r"\[.*\]", output, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    return []


# ===============================
# 🔹 NORMALIZER
# ===============================
def normalize_task(task):
    task = task.lower().strip()

    mapping = {
        "fetch movies": "Fetch movies",
        "get ratings": "Get ratings",
        "analyze reviews": "Analyze reviews",
        "generate summary": "Generate summary",
        "select event": "Select event",
        "book venue": "Book venue",
        "send invitations": "Send invitations",
        "finalize schedule": "Finalize schedule"
    }

    return mapping.get(task, None)


# ===============================
# 🔹 AGENT CLASS
# ===============================
class PlannerAgent:

    def __init__(self):
        self.knowledge_base = self.load_kb()

    def load_kb(self):
        try:
            with open("knowledge_base/data.json", "r") as f:
                return json.load(f)
        except:
            return {}

    # ---------------------------
    # LLM PLANNER (STRICT JSON)
    # ---------------------------
    def decompose_goal(self, goal):

        prompt = f"""
You are an AI planner.

Convert the goal into a STRICT JSON ARRAY of tasks.

Goal: {goal}

Allowed tasks:
{ALLOWED_TASKS}

RULES:
- Output ONLY JSON array
- No explanation
- No extra text
- Example output:
["Fetch movies", "Get ratings", "Analyze reviews", "Generate summary"]
"""

        output = call_ollama(prompt)
        print("\n[Raw Model Output]:", output)

        tasks = parse_model_output(output)

        if not tasks:
            return fallback_logic(goal)

        return tasks

    # ---------------------------
    # VALIDATION
    # ---------------------------
    def validate_tasks(self, tasks):
        fixed = []

        for t in tasks:
            norm = normalize_task(t)
            if norm and norm in ALLOWED_TASKS:
                fixed.append(norm)

        return fixed

    # ---------------------------
    # COMPLETENESS CHECK
    # ---------------------------
    def ensure_completeness(self, goal, tasks):

        goal = goal.lower()

        if "movie" in goal:
            required = [
                "Fetch movies",
                "Get ratings",
                "Analyze reviews",
                "Generate summary"
            ]
        elif "event" in goal:
            required = [
                "Select event",
                "Book venue",
                "Send invitations",
                "Finalize schedule"
            ]
        else:
            return tasks

        if len(set(tasks) & set(required)) < 3:
            return required

        return tasks

    # ---------------------------
    # MAIN PIPELINE
    # ---------------------------
    def plan(self, goal):

        print("\n[Agent] Thinking using Ollama...")

        tasks = self.decompose_goal(goal)

        print("[Agent] Validating tasks...")
        tasks = self.validate_tasks(tasks)

        print("[Agent] Ensuring completeness...")
        tasks = self.ensure_completeness(goal, tasks)

        if not tasks:
            tasks = fallback_logic(goal)

        print("[Agent] Planning execution...")

        return tasks


# ===============================
# 🔹 RUNNER
# ===============================
if __name__ == "__main__":

    print("=" * 50)
    print("🎯 ENTERTAINMENT PLANNING AGENT (V3 - QWEN READY)")
    print("=" * 50)

    agent = PlannerAgent()

    goal = input("\nEnter your goal: ")
    result = agent.plan(goal)

    print("\n📌 FINAL PLAN:")
    for i, task in enumerate(result, 1):
        print(f"{i}. {task}")