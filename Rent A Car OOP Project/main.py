from rent_a_car_system import RentACarSystem

def main():
    system = RentACarSystem()

    # Load saved data (if any) from CSV files
    system.load_data()

    while True:
        print("\n--- Rent A Car System ---")
        print("1. Display Available Cars")
        print("2. Display All Cars")
        print("3. Display Cars by Category")
        print("4. Rent a Car")
        print("5. Return a Car")
        print("6. Add a New Car")
        print("7. Add a New Customer")
        print("8. Save and Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            system.display_available_cars()
        elif choice == "2":
            system.display_all_cars()
        elif choice == "3":
            system.display_cars_by_category()
        elif choice == "4":
            system.rent_car()
        elif choice == "5":
            system.return_car()
        elif choice == "6":
            system.add_car()
        elif choice == "7":
            system.add_customer()
        elif choice == "8":
            system.save_data()
            print("Data saved. Exiting system...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
