import csv

def get_hotels(city):
    hotels = []
    try:
        with open('hotel_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'].lower() == city.lower():
                    hotels.append((row['hotel_name'], int(row['price'])))
    except Exception as e:
        print(f"Error reading hotel data: {e}")
    return hotels

def main():
    print("Hotel Agent: Enter a city to get hotel list.")
    while True:
        city = input("City (or 'exit' to quit): ")
        if city.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        hotels = get_hotels(city)
        if hotels:
            print(f"Hotels in {city}:")
            for name, price in hotels:
                print(f"- {name}: ₹{price}")
        else:
            print(f"No hotel data found for {city}.")

if __name__ == "__main__":
    main()
