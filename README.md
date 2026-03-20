# Python Hello World Agent Project

This project demonstrates a simple Python agent that interacts with a locally installed Ollama LLM (llama3.2) to generate responses based on user input.

## Features
- Simple Hello World script
- Agent that sends user input to a local LLM and prints the response

## Requirements
- Python 3.8+
- requests (for HTTP API calls)
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
   - Ollama should be installed at `C:\Users\Gourav\AppData\Local\Programs\Ollama`.
   - Start Ollama server if not already running.
   - Pull llama3.2 model if needed:
     ```sh
     ollama pull llama3.2
     ```

## Usage
Run the agent script:
```sh
python agent_hello.py
```

You will be prompted to enter a message. The agent will send it to the local Ollama llama3.2 model and print the response.

---
This project is for demonstration purposes. Replace the Ollama model name or API endpoint as needed for your setup.
