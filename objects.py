def eat():
    print("I am eating")

class Person:

    name = "Ice"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating right now")

class Animal:

    def __init__(self, animal_type):
        self.type = animal_type

    def action(self):
        if self.type == 'Predator':
            print(f"{self.type} is hunting")

        if self.type == 'Prey':
            print(f"{self.type} is hiding")

eat()
person_1 = Person("Ice")
person_2 = Person("Daniel")
person_1.eat()
person_2.eat()

# > ---

bunny = Animal("Prey")
lion = Animal("Predator")
bunny.action()
lion.action()

# > attributes --- 
print(person_1.name)