
# Define the parent class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Parent class method
    def start_engine(self):
        print("Starting engine...")

# Define the first child class
class Car(Vehicle):
    def __init__(self, make, model, year, num_of_doors):
        Vehicle.__init__(self, make, model, year)
        self.num_of_doors = num_of_doors

    # Child class method that uses polymorphism on the parent class method
    def start_engine(self):
        print("Turning the key...")
        Vehicle.start_engine(self)

# Define the second child class
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_of_wheels):
        Vehicle.__init__(self, make, model, year)
        self.num_of_wheels = num_of_wheels

    # Child class method that uses polymorphism on the parent class method
    def start_engine(self):
        print("Kicking the start lever...")
        Vehicle.start_engine(self)

# Create instances of each class and call the start_engine method
car = Car("Toyota", "Camry", 2020, 4)
car.start_engine()
print()
motorcycle = Motorcycle("Harley Davidson", "Road King", 2022, 2)
motorcycle.start_engine()
