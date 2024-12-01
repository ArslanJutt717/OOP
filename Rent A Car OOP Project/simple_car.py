from car import Car

class SimpleCar(Car):
    def __init__(self, car_id, model, brand, rental_rate):
        super().__init__(car_id, model, brand, rental_rate, "Simple")

    def __str__(self):
        return f"[Simple Car] {super().__str__()}"