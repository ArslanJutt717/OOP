from sport_car import SportsCar
from simple_car import SimpleCar
from royal_car import RoyalCar
from customer import Customer
from file_handler import FileHandler

class RentACarSystem:
    def __init__(self):
        self.__cars = []
        self.__customers = []

    def display_available_cars(self):
        print("\n--- Available Cars ---")
        for car in self.__cars:
            if not car.is_rented():
                print(car)

    def display_all_cars(self):
        print("\n--- All Cars ---")
        for car in self.__cars:
            print(car)

    def display_cars_by_category(self):
        print("\n--- Choose Car Category ---")
        print("1. Sports")
        print("2. Simple")
        print("3. Royal")
        category_choice = input("Enter your choice (1-3): ")

        if category_choice == "1":
            category = "Sports"
        elif category_choice == "2":
            category = "Simple"
        elif category_choice == "3":
            category = "Royal"
        else:
            print("Invalid choice.")
            return

        print(f"\n--- Available {category} Cars ---")
        available_cars = [car for car in self.__cars if car.get_category() == category and not car.is_rented()]

        if available_cars:
            for car in available_cars:
                print(car)
        else:
            print(f"No available {category} cars at the moment.")

    def rent_car(self):
        try:
            customer_id = int(input("Enter Customer ID: "))
            car_id = int(input("Enter Car ID: "))

            customer = next((c for c in self.__customers if c.get_customer_id() == customer_id), None)
            if not customer:
                print("Invalid Customer ID. No such customer found.")
                return

            car = next((c for c in self.__cars if c.get_car_id() == car_id), None)
            if not car:
                print("Invalid Car ID. No car found with the given ID.")
            elif car.is_rented():
                print(f"The car {car.get_model()} {car.get_brand()} is already rented.")
            else:
                customer.set_rented_car_id(car_id)
                car.set_rented_status(True)
                print(f"{customer.get_name()} successfully rented {car.get_brand()} {car.get_model()}.")
        except ValueError:
            print("Please enter valid numbers for Customer ID and Car ID.")

    def return_car(self):
        try:
            customer_id = int(input("Enter Customer ID to return the car: "))
            customer = next((c for c in self.__customers if c.get_customer_id() == customer_id), None)

            if customer and customer.get_rented_car_id():
                car_id = customer.get_rented_car_id()
                car = next((c for c in self.__cars if c.get_car_id() == car_id), None)
                if car:
                    car.set_rented_status(False)
                customer.set_rented_car_id(None)
                print(f"{customer.get_name()} has returned the car.")
            else:
                print("No car rented by this customer.")
        except ValueError:
            print("Please enter a valid Customer ID.")

    def add_car(self):
        try:
            car_id = int(input("Enter Car ID: "))
            model = input("Enter Model: ")
            brand = input("Enter Brand: ")
            rental_rate = float(input("Enter Rental Rate per day: "))

            print("Choose Car Category:")
            print("1. Sports")
            print("2. Simple")
            print("3. Royal")
            category_choice = input("Enter your choice (1-3): ")

            if category_choice == "1":
                car = SportsCar(car_id, model, brand, rental_rate)
            elif category_choice == "2":
                car = SimpleCar(car_id, model, brand, rental_rate)
            elif category_choice == "3":
                car = RoyalCar(car_id, model, brand, rental_rate)
            else:
                print("Invalid choice. Adding as Simple Car by default.")
                car = SimpleCar(car_id, model, brand, rental_rate)

            self.__cars.append(car)
            print(f"{car.get_brand()} {car.get_model()} added successfully.")
        except ValueError:
            print("Invalid input. Please enter valid values for car ID and rental rate.")

    def add_customer(self):
        try:
            customer_id = int(input("Enter Customer ID: "))
            name = input("Enter Customer Name: ")
            customer = Customer(customer_id, name)
            self.__customers.append(customer)
            print(f"Customer {name} added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid customer ID.")
    
    def save_data(self):
        FileHandler.save_cars(self.__cars)
        FileHandler.save_customers(self.__customers)
        print("Data saved successfully.")

    def load_data(self):
        self.__cars = FileHandler.load_cars()
        self.__customers = FileHandler.load_customers()
        print("Data loaded successfully.")
