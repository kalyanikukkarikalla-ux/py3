from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


# Full-time Employee class
class FullTimeEmployee(Employee):
    def __init__(self):
        self.monthly_salary = 50000

    def calculate_salary(self):
        print("Full-Time Employee Salary: ₹", self.monthly_salary)


# Part-time Employee class
class PartTimeEmployee(Employee):
    def __init__(self):
        self.hours_worked = 80
        self.rate_per_hour = 300

    def calculate_salary(self):
        salary = self.hours_worked * self.rate_per_hour
        print("Part-Time Employee Salary: ₹", salary)


# Main program
e1 = FullTimeEmployee()
e2 = PartTimeEmployee()

e1.calculate_salary()
e2.calculate_salary()