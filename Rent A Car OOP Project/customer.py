class Customer:
    def __init__(self, customer_id, name):
        self.__customer_id = customer_id
        self.__name = name
        self.__rented_car_id = None

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_rented_car_id(self):
        return self.__rented_car_id

    def set_rented_car_id(self, car_id):
        self.__rented_car_id = car_id

    def __str__(self):
        return f"Customer ID: {self.__customer_id}, Name: {self.__name}, Rented Car ID: {self.__rented_car_id if self.__rented_car_id else 'None'}"
