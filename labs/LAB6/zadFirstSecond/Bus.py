from labs.LAB6.zadFirstSecond.Vehicle import Vehicle

#zad2


class Bus(Vehicle):
    def __init__(self, seats_number, max_speed, mileage, model_name):
        self.seats_number = seats_number
        super().__init__(max_speed, mileage, model_name)

    def print_info(self):
        super().print_info()
        print("Seats: ", self.seats_number)


my_bus = Bus(10, 10, 150, "Mercedes")
my_bus.print_info()
