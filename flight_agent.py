import csv

def get_flight_cost(from_city, to_city):
    try:
        with open('flight_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['from_city'].lower() == from_city.lower() and row['to_city'].lower() == to_city.lower():
                    return int(row['price'])
        return None
    except Exception as e:
        print(f"Error reading flight data: {e}")
        return None

def main():
    print("Flight Agent: Enter cities to get flight cost.")
    while True:
        from_city = input("From city (or 'exit' to quit): ")
        if from_city.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        to_city = input("To city: ")
        if to_city.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        cost = get_flight_cost(from_city, to_city)
        if cost is not None:
            print(f"Cost of flight from {from_city} to {to_city}: ₹{cost}")
        else:
            print(f"No flight data found for {from_city} to {to_city}.")

if __name__ == "__main__":
    main()
