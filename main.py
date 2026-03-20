import requests
import sys
import flight_agent
import hotel_agent
import time

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

def call_llm(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    start_time = time.time()
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        llm_response = data.get("response", "")
        elapsed = time.time() - start_time
        return llm_response, elapsed
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return "", 0

def main():
    print("Main Agent: Enter your prompt (e.g., 'Get flight cost from Delhi to Mumbai' or 'List hotels in Bangalore').")
    while True:
        user_prompt = input("Prompt (or 'exit' to quit): ")
        if user_prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        llm_response, elapsed = call_llm(user_prompt)
        print(f"LLM response time: {elapsed:.2f} seconds")
        # Simple keyword-based routing based on LLM response
        if "flight" in llm_response.lower():
            print("Intention: Call flight agent")
            # Extract cities (simple parsing, can be improved)
            words = user_prompt.split()
            from_city, to_city = None, None
            for i, w in enumerate(words):
                if w.lower() == "from" and i+1 < len(words):
                    from_city = words[i+1]
                if w.lower() == "to" and i+1 < len(words):
                    to_city = words[i+1]
            if from_city and to_city:
                cost = flight_agent.get_flight_cost(from_city, to_city)
                if cost is not None:
                    print(f"Flight cost from {from_city} to {to_city}: ₹{cost}")
                    # Now show hotels in destination city
                    print(f"\nHotels available in {to_city}:")
                    hotels = hotel_agent.get_hotels(to_city)
                    if hotels:
                        for name, price in hotels:
                            print(f"- {name}: ₹{price}")
                    else:
                        print(f"No hotel data found for {to_city}.")
                else:
                    print(f"No flight data found for {from_city} to {to_city}.")
            else:
                print("Could not parse cities from prompt.")
        elif "hotel" in llm_response.lower():
            print("Intention: Call hotel agent")
            # Extract city (simple parsing, can be improved)
            words = user_prompt.split()
            city = None
            for i, w in enumerate(words):
                if w.lower() == "in" and i+1 < len(words):
                    city = words[i+1]
            if city:
                hotels = hotel_agent.get_hotels(city)
                if hotels:
                    print(f"Hotels in {city}:")
                    for name, price in hotels:
                        print(f"- {name}: ₹{price}")
                else:
                    print(f"No hotel data found for {city}.")
            else:
                print("Could not parse city from prompt.")
        else:
            print("LLM could not determine agent. Please rephrase your prompt.")

if __name__ == "__main__":
    main()
