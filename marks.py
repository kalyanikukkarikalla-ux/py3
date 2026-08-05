class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return f"name:{self.name}, roll:{self.roll}, marks:{self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.roll}, {self.marks})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.roll == other.roll
        return False


s1 = Student("Kalyani", 101, 90)
s2 = Student("Kalyani", 101, 95)
s3 = Student("Chinni", 102, 90)

print(s1)
print(repr(s1))
print(s1 == s2)
print(s1 == s3)