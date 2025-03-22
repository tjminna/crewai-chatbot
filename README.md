# ISMAgent Chatbot

## Overview
ISMAgent Chatbot is an intelligent conversational AI built with Streamlit, CrewAI, MongoDB, and OpenAI's GPT model. It's designed to assist users by clearly and intelligently answering their queries. The chatbot retains memory about its identity and creator through MongoDB integration, enhancing interactions with personalized context.

## Features
- **Conversational AI** powered by CrewAI and OpenAI's GPT-4o-mini model.
- **Memory integration** via MongoDB, storing agent details and ensuring persistent identity.
- **Intuitive UI** built using Streamlit for seamless user interaction.
- **Easily extendable** architecture for additional functionality or customization.

## Installation
### Prerequisites
- Python 3.8+
- MongoDB (Running locally or remotely)

### Clone the Repository
```bash
git clone <your-repository-url>
cd ISMAgent-Chatbot
```

### Install Dependencies
```bash
pip install streamlit pymongo crewai langchain openai
```

## Setup
### MongoDB Configuration
Ensure MongoDB is running and accessible. The default setup connects to `mongodb://localhost:27017/`.

### OpenAI API Key
Create a `.env` file or set an environment variable with your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key'
```

### Backstory Setup
Add your agent's backstory in a file named `backstory.txt` in the project root directory.

## Running the Chatbot
```bash
streamlit run your_script.py
```
Access your chatbot through `http://localhost:8501`.

## Project Structure
```
.
├── backstory.txt
├── your_script.py
├── .env (optional)
└── README.md
```

## Usage
Interact with the chatbot directly via the Streamlit interface by entering your questions and receiving clear, context-aware responses.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- **Minna T J**
- **Institution**: IIT Dhanbad