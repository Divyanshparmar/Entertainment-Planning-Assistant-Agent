import sys
import os
import time

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from agent.planner import PlannerAgent
from tools import movie_tools
from scheduler.scheduler import Scheduler


# 🔥 Dynamic Tool Mapping (No hardcoding)
TOOL_MAP = {
    "Fetch movies": movie_tools.fetch_movies,
    "Get ratings": movie_tools.get_ratings,
    "Analyze reviews": movie_tools.analyze_reviews,
    "Generate summary": movie_tools.generate_summary,

    "Select event": movie_tools.select_event,
    "Book venue": movie_tools.book_venue,
    "Send invitations": movie_tools.send_invitations,
    "Finalize schedule": movie_tools.finalize_schedule
}


def execute_task(task):
    func = TOOL_MAP.get(task)
    if func:
        print(f"[Executing] {task}...")
        return func()
    return "❌ No tool found"


def main():
    print("=" * 50)
    print("🎯 ENTERTAINMENT PLANNING AGENT")
    print("=" * 50)

    goal = input("\nEnter your goal: ")

    start = time.time()

    # 🔹 Planning
    agent = PlannerAgent()
    tasks = agent.plan(goal)

    if not tasks or "Unknown Goal" in tasks:
        print("\n❌ Unable to process goal.")
        print("👉 Try: 'Movie review' or 'Event planning'")
        return

    print("\n📌 Planned Tasks:")
    for t in tasks:
        print(f"• {t}")

    # 🔹 Scheduling
    scheduler = Scheduler()
    schedule = scheduler.create_schedule(tasks)

    print("\n📅 Execution Schedule:")
    for i, task in enumerate(schedule, 1):
        print(f"{i}. {task}")

    # 🔹 Execution
    print("\n⚙️ Executing Tasks:")
    print("-" * 40)

    for task in schedule:
        result = execute_task(task)
        print(f"{task} → {result}")

    end = time.time()

    print("-" * 40)
    print(f"\n⏱ Execution Time: {round(end - start, 2)} seconds")
    print("=" * 50)


if __name__ == "__main__":
    main()