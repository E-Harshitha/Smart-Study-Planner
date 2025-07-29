import streamlit as st
import requests

st.title("📚 Smart Study Planner")

# --- Form to input subjects and durations ---
st.subheader("📝 Create Your Own Study Plan")

with st.form("study_plan_form"):
    subject1 = st.text_input("Subject 1", value="Math")
    duration1 = st.text_input("Duration 1", value="2 hours")

    subject2 = st.text_input("Subject 2", value="Physics")
    duration2 = st.text_input("Duration 2", value="1.5 hours")

    subject3 = st.text_input("Subject 3", value="Break")
    duration3 = st.text_input("Duration 3", value="30 minutes")

    submitted = st.form_submit_button("Generate Plan")

# --- Display the custom plan if submitted ---
if submitted:
    custom_plan = [
        {"subject": subject1, "duration": duration1},
        {"subject": subject2, "duration": duration2},
        {"subject": subject3, "duration": duration3},
    ]

    st.success("✅ Your Custom Study Plan:")
    for item in custom_plan:
        st.write(f"**{item['subject']}** — {item['duration']}")

# --- Optionally fetch default plan from backend ---
st.divider()
st.subheader("📦 Default Plan from Backend")

try:
    response = requests.get("http://localhost:8000/study-plan")
    data = response.json()
    for item in data["plan"]:
        st.write(f"**{item['subject']}** — {item['duration']}")
except Exception as e:
    st.error(f"Failed to fetch default plan: {e}")