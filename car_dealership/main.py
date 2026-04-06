from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                      get_car_by_id, update_car, delete_car, search_cars)

def show_menu():
    print("\n" + "="*40)
    print(" 🚗 CAR DEALERSHIP MANAGER")
    print("="*40)
    print("1. Add Car")
    print("2. View All Cars")
    print("3. Update Car")
    print("4. Delete Car")
    print("5. Search Cars")
    print("6. Exit")
    return input("Choose an option (1-6): ")

def add_car_flow():
    print("\n➕ Add a New Car")

    try:
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = float(input("Price: "))
        mileage = int(input("Mileage: "))

        car = Car(make, model, year, price, mileage)
        add_car(car)

        print(f"Car added successfully! Assigned ID: {car.id}")

    except ValueError:
        print("Invalid input. Please enter numbers for year, price, and mileage.")

def view_all_cars_flow():
    print("\n📋 All Cars in Inventory")
    cars = get_all_cars()

    if not cars:
        print("No cars in inventory.")
    else:
        for car in cars:
            print(car)

    input("\nPress Enter to return to the menu...")

def update_car_flow():
    print("\n✏️ Update a Car")

    try:
        car_id = int(input("Enter car ID to update: "))
    except ValueError:
        print("Invalid ID format.")
        return
    
    car = get_car_by_id(car_id)
    if not car:
        print("Car not found.")
        return
    
    print("Current car details:")
    print(car)

    if new_price := input(f"Price [{car.price}]: "):
        try:
            car.price = float(new_price)
        except ValueError:
            print("Price must be a number, ignoring that change.")

    if new_mileage := input(f"Mileage [{car.mileage}]: "):
        try:
            car.mileage = int(new_mileage)
        except ValueError:
            print("Mileage must be a number, ignoring that change.")

    update_car(car)
    print("Car updated successfully!")

def delete_car_flow():
    print("\n🗑️ Delete a Car")

    try:
        car_id = int(input("Enter car ID to delete: "))
    except ValueError:
        print("Invalid ID format.")
        return
    
    car = get_car_by_id(car_id)
    if not car:
        print("Car not found.")
        return
    
    print(f"Car to delete: {car}")
    confirm = input("Are you sure you want to delete this car? (y/n): ").lower()

    if confirm == 'y':
        delete_car(car_id)
        print("Car deleted successfully!")
    else:
        print("Delete cancelled.")

def search_cars_flow():
    print("\n🔍 Search Cars")
    keyword = input("Enter search term: ")
    results = search_cars(keyword)

    if not results:
        print("No matches found.")
    else:
        print(f"Found {len(results)} car(s):\n")
        for car in results:
            print(car)
    
    input("\nPress Enter to return to the menu...")

def main():
    initialize_database()
    import_cars()

    while True:
        choice = show_menu()

        if choice == "1":
            add_car_flow()

        elif choice == "2":
            view_all_cars_flow()

        elif choice == "3":
            update_car_flow()

        elif choice == "4":
            delete_car_flow()

        elif choice == "5":
            search_cars_flow()

        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
