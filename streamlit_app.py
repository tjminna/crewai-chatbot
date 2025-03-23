# SQLite fix for ChromaDB
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


import streamlit as st
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# === In-memory agent details ===
memory = {
    "agent_name": "ISMAgent",
    "built_by": "Minna T J",
    "works_at": "IIT Dhanbad"
}

# === Load backstory ===
with open("backstory.txt", "r", encoding="utf-8") as f:
    backstory = f.read()

# === Create CrewAI Agent ===
def create_crew_agent(memory):
    system_prompt = (
        f"You are {memory['agent_name']}, an AI assistant built by {memory['built_by']} "
        f"at {memory['works_at']}. Answer questions clearly and helpfully."
    )

    return Agent(
        role="ISM Agent",
        goal="Answer questions and assist users clearly and intelligently.",
        backstory=backstory,
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model=os.getenv("MODEL")),
        system_prompt=system_prompt
    )

# === Chat function using CrewAI Task ===
def get_agent_response(agent, message):
    task = Task(
        description=message,
        expected_output="A helpful and accurate response to the user's question. If user asks unrelated questions, politely redirect them to the right topic.",
        agent=agent
    )
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )
    result = crew.kickoff()
    return result

# === Streamlit UI ===
st.set_page_config(page_title="ISMAgent Chatbot", page_icon="🤖")
st.title("🤖 ISMAgent Chatbot")

# Load agent
agent = create_crew_agent(memory)

# User input and response
user_input = st.text_input("You:", "")
if user_input:
    response = get_agent_response(agent, user_input)
    st.markdown(f"**ISMAgent:** {response}")