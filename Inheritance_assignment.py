
# Define the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print("Name:", self.name)
        print("Species:", self.species)

# Define the first child class
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def display_info(self):
        Animal.display_info(self)
        print("Breed:", self.breed)

# Define the second child class
class Cat(Animal):
    def __init__(self, name, fur_color):
        Animal.__init__(self, name, species="Cat")
        self.fur_color = fur_color

    def display_info(self):
        Animal.display_info(self)
        print("Fur Color:", self.fur_color)

# Create an instance of each class and display their information
dog = Dog("Fido", "Labrador")
dog.display_info()
print()
cat = Cat("Fluffy", "White")
cat.display_info()
