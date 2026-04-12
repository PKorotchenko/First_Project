from models import PriceTracker

def main():
    tracker = PriceTracker()

    while True:
        print("\nFood Price Tracker")
        print("1. Add Store")
        print("2. View Stores")
        print("3. Add Food Item")
        print("4. View Food Items")
        print("5. Get Average Price for Item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Store name: ")
            location = input("Store location: ")
            tracker.add_store(name, location)
            print("Store added.")

        elif choice == '2':
            stores = tracker.get_stores()
            if stores:
                for store in stores:
                    print(f"ID: {store[0]}, Name: {store[1]}, Location: {store[2]}")
            else:
                print("No stores found.")

        elif choice == '3':
            stores = tracker.get_stores()
            if not stores:
                print("No stores available. Add a store first.")
                continue
            print("Available stores:")
            for store in stores:
                print(f"ID: {store[0]}, Name: {store[1]}")
            store_id = int(input("Enter store ID: "))
            name = input("Food item name: ")
            price = float(input("Price: "))
            tracker.add_food_item(name, price, store_id)
            print("Food item added.")

        elif choice == '4':
            items = tracker.get_food_items()
            if items:
                for item in items:
                    print(f"Item: {item[0]}, Price: ${item[1]:.2f}, Date: {item[2]}, Store: {item[3]}")
            else:
                print("No food items found.")

        elif choice == '5':
            item_name = input("Enter food item name: ")
            avg_price = tracker.get_average_price(item_name)
            if avg_price:
                print(f"Average price for {item_name}: ${avg_price:.2f}")
            else:
                print("No data found for that item.")

        elif choice == '6':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()