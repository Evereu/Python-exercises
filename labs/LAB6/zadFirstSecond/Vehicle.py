



class Vehicle:
    def __init__(self, max_speed, mileage, model_name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.model_name = model_name

    def print_info(self):
        print("Max speed: ", self.max_speed)
        print("Mileage: ", self.mileage)
        print("Model Name: ", self.model_name)


my_vehicle = Vehicle(10, 150, "Mercedes")
my_vehicle.print_info()

