import streamlit as st
from pymongo import MongoClient
from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI
import os


with open("backstory.txt", "r") as f:
    backstory = f.read()

# === Load memory from MongoDB ===
def get_agent_memory():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ism_chatbot"]
    collection = db["agent_info"]

    if collection.count_documents({"agent_name": "ISMAgent"}) == 0:
        collection.insert_one({
            "agent_name": "ISMAgent",
            "built_by": "Minna T J",
            "works_at": "IIT Dhanbad"
        })

    agent_data = collection.find_one({"agent_name": "ISMAgent"})
    return {
        "agent_name": agent_data["agent_name"],
        "built_by": agent_data["built_by"],
        "works_at": agent_data["works_at"]
    }

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
        llm=ChatOpenAI(model="gpt-4o-mini"),
        system_prompt=system_prompt
    )

# === Chat function using CrewAI Task ===
def get_agent_response(agent, message):
    task = Task(
        description=message,
        expected_output="A helpful and accurate response to the user's question. If user ask unrelated questions, you should politely redirect them to the right topic.",
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

# Load memory and agent
memory = get_agent_memory()
agent = create_crew_agent(memory)

# User input and response
user_input = st.text_input("You:", "")
if user_input:
    response = get_agent_response(agent, user_input)
    st.markdown(f"**ISMAgent:** {response}")
