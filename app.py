import streamlit as st
from agent.planner import PlannerAgent

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="AI Planning Agent",
    page_icon="🎯",
    layout="centered"
)

# Initialize agent
agent = PlannerAgent()

# ----------------------------
# Title Section
# ----------------------------
st.title("🎯 AI Planning Agent")
st.caption("Turn your goal into a step-by-step execution plan")

# ----------------------------
# Session State
# ----------------------------
if "plan" not in st.session_state:
    st.session_state.plan = None

# ----------------------------
# Input Form (Better UX)
# ----------------------------
with st.form("goal_form"):
    goal = st.text_input("Enter your goal", placeholder="e.g. Analyze popular movies, Plan event, etc.")
    submitted = st.form_submit_button("Generate Plan 🚀")

# ----------------------------
# Generate Plan
# ----------------------------
if submitted:

    if not goal.strip():
        st.warning("⚠️ Please enter a valid goal")
    else:
        try:
            with st.spinner("🧠 AI Agent is thinking..."):
                st.session_state.plan = agent.plan(goal)

            st.success("Plan Generated Successfully!")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

# ----------------------------
# Output Section
# ----------------------------
if st.session_state.plan:

    st.subheader("📌 Final Plan")

    # Display as nice cards
    for i, task in enumerate(st.session_state.plan, 1):
        with st.container():
            st.markdown(
                f"""
                <div style="
                    padding:10px;
                    margin:5px 0px;
                    border-radius:10px;
                    background-color:#1e1e1e;
                    border:1px solid #333;
                ">
                    <b>Step {i}</b><br>
                    {task}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Expandable raw output
    with st.expander("🔍 View Raw Output"):
        st.write(st.session_state.plan)

    # Reset button
    if st.button("🔄 Clear Plan"):
        st.session_state.plan = None
        st.rerun()