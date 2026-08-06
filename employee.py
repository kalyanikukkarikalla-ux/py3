class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.id == other.id


# Creating objects
emp1 = Employee(101, "Rahul", 50000)
emp2 = Employee(101, "Rahul", 60000)
emp3 = Employee(102, "Anil", 50000)

# Comparing objects using __eq__()
print(emp1 == emp2)
print(emp1 == emp3)