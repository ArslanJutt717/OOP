class Car:
    def __init__(self, car_id, model, brand, rental_rate, category):
        self.__car_id = car_id
        self.__model = model
        self.__brand = brand
        self.__rental_rate = rental_rate
        self.__category = category
        self.__is_rented = False

    def get_car_id(self):
        return self.__car_id

    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand

    def get_rental_rate(self):
        return self.__rental_rate

    def get_category(self):
        return self.__category

    def is_rented(self):
        return self.__is_rented

    def set_rented_status(self, status):
        self.__is_rented = status

    def __str__(self):
        rented_status = "Yes" if self.__is_rented else "No"
        return (f"Car ID: {self.__car_id}, Model: {self.__model}, Brand: {self.__brand}, "
                f"Category: {self.__category}, Rental Rate: ${self.__rental_rate}/day, Rented: {rented_status}")
