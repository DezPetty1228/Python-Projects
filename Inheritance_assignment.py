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
    def __init__(self, name, breed, num_of_legs=4):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        self.num_of_legs = num_of_legs

    def display_info(self):
        Animal.display_info(self)
        print("Breed:", self.breed)
        print("Number of Legs:", self.num_of_legs)

# Define the second child class
class Cat(Animal):
    def __init__(self, name, fur_color, num_of_lives=9):
        Animal.__init__(self, name, species="Cat")
        self.fur_color = fur_color
        self.num_of_lives = num_of_lives

    def display_info(self):
        Animal.display_info(self)
        print("Fur Color:", self.fur_color)
        print("Number of Lives:", self.num_of_lives)

# Create an instance of each class and display their information
dog = Dog("Fido", "Labrador")
dog.display_info()
print()
cat = Cat("Fluffy", "White")
cat.display_info()
