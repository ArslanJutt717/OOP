import csv
from car import Car
from customer import Customer

class FileHandler:
    @staticmethod
    def save_cars(cars):
        with open('cars.csv', mode='w', newline='') as car_file:
            writer = csv.writer(car_file)
            writer.writerow(['Car ID', 'Model', 'Brand', 'Rental Rate', 'Category', 'Is Rented'])
            for car in cars:
                writer.writerow([
                    car.get_car_id(),
                    car.get_model(),
                    car.get_brand(),
                    car.get_rental_rate(),
                    car.get_category(),
                    car.is_rented()
                ])

    @staticmethod
    def save_customers(customers):
        with open('customers.csv', mode='w', newline='') as customer_file:
            writer = csv.writer(customer_file)
            writer.writerow(['Customer ID', 'Name', 'Rented Car ID'])
            for customer in customers:
                writer.writerow([
                    customer.get_customer_id(),
                    customer.get_name(),
                    customer.get_rented_car_id()
                ])

    @staticmethod
    def load_cars():
        cars = []
        try:
            with open('cars.csv', mode='r') as car_file:
                reader = csv.DictReader(car_file)
                for row in reader:
                    car = Car(
                        int(row['Car ID']),
                        row['Model'],
                        row['Brand'],
                        float(row['Rental Rate']),
                        row['Category']
                    )
                    car.set_rented_status(row['Is Rented'] == 'True')
                    cars.append(car)
        except FileNotFoundError:
            print("No car data found. Starting fresh.")
        return cars

    @staticmethod
    def load_customers():
        customers = []
        try:
            with open('customers.csv', mode='r') as customer_file:
                reader = csv.DictReader(customer_file)
                for row in reader:
                    customer = Customer(int(row['Customer ID']), row['Name'])
                    if row['Rented Car ID']:
                        customer.set_rented_car_id(int(row['Rented Car ID']))
                    customers.append(customer)
        except FileNotFoundError:
            print("No customer data found. Starting fresh.")
        return customers
