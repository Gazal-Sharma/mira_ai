import streamlit as st
from mira_sdk import MiraClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

st.title("Personalized Study Planner")

subjects = st.text_area("Enter subjects and difficulty:", "Math: Hard, Physics: Medium, Chemistry: Easy")
hours = st.number_input("Total available study hours:", min_value=1, max_value=50, value=10)

if st.button("Generate Study Plan"):
    if subjects and hours:
        input_data = {"subjects": subjects, "hours": hours}
        response = client.flow.execute("gazal-sh/StudyPlanner", input_data)
        st.write(response.get("result", "No response from Mira AI"))
    else:
        st.warning("Please enter subjects and hours.")
