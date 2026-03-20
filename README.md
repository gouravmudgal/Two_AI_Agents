# Two AI Agents Project

This project demonstrates a multi-agent system using Python and Ollama LLM. It features a main agent that interprets user prompts and routes them to specialized agents: a flight agent for retrieving flight costs between cities and a hotel agent for listing hotels in a city. The agents use local CSV data files for information.

## Features
- Main agent that uses Ollama LLM to understand user intentions
- Flight agent: Retrieves flight costs between cities from `flight_data.csv`
- Hotel agent: Lists available hotels and prices in a city from `hotel_data.csv`
- Simple keyword-based routing based on LLM response
- Interactive command-line interface

## Requirements
- Python 3.8+
- requests (for HTTP API calls to Ollama)
- Ollama (llama3.2 model installed locally)

## Setup
1. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and running locally with the llama3.2 model:
   - Install Ollama from [ollama.ai](https://ollama.ai)
   - Start Ollama server if not already running
   - Pull llama3.2 model if needed:
     ```sh
     ollama pull llama3.2
     ```

## Usage
Run the main agent script:
```sh
python main.py
```

You will be prompted to enter a message. Examples:
- "Get flight cost from Delhi to Mumbai"
- "List hotels in Bangalore"

The main agent sends the prompt to the local Ollama llama3.2 model, interprets the response, and routes to the appropriate specialized agent.

### Individual Agents
You can also run the agents individually:
- Flight agent: `python flight_agent.py`
- Hotel agent: `python hotel_agent.py`

## Data Files
- `flight_data.csv`: Contains flight information with columns: from_city, to_city, price
- `hotel_data.csv`: Contains hotel information with columns: city, hotel_name, price

## Project Structure
- `main.py`: Main agent script with LLM integration and routing
- `flight_agent.py`: Flight cost retrieval agent
- `hotel_agent.py`: Hotel listing agent
- `agent_hello.py`: Simple hello world agent (legacy)
- `flight_data.csv`: Flight data
- `hotel_data.csv`: Hotel data
- `requirements.txt`: Python dependencies

---
This project is for demonstration purposes. The LLM routing is basic and can be improved with more advanced NLP techniques.
