from car import Car

class SportsCar(Car):
    def __init__(self, car_id, model, brand, rental_rate):
        super().__init__(car_id, model, brand, rental_rate, "Sports")

    def __str__(self):
        return f"[Sports Car] {super().__str__()}"
