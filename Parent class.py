# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class Dog
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child class Cat
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Child class Cow
class Cow(Animal):
    def sound(self):
        print("Cow moos")


# Main program
a = Dog()
a.sound()

a = Cat()
a.sound()

a = Cow()
a.sound()