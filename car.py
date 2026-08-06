class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# Creating object
car1 = Car("Toyota", "Fortuner", 2024)

# Calling __str__ automatically
print(car1)