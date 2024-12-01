from car import Car

class RoyalCar(Car):
    def __init__(self, car_id, model, brand, rental_rate):
        super().__init__(car_id, model, brand, rental_rate, "Royal")

    def __str__(self):
        return f"[Royal Car] {super().__str__()}"
