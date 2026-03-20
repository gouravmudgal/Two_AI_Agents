import requests

# Ollama local API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"
# Model name for llama3.2
MODEL_NAME = "llama3.2"

def main():
    print("Hello, World! This is your Ollama llama3.2 agent.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        payload = {
            "model": MODEL_NAME,
            "prompt": user_input,
            "stream": False
        }
        try:
            response = requests.post(OLLAMA_API_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            print("Agent:", data.get("response", "[No response]").strip())
        except Exception as e:
            print(f"Error communicating with Ollama: {e}")

if __name__ == "__main__":
    main()
