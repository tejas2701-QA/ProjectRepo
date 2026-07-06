class Developer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Developer {self.name} is {self.age} years old"

d1 = Developer("John", 18)
print(d1)
d2 = Developer("Ram", 34)
print(d2)
