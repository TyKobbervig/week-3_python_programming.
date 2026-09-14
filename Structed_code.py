class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " is barking.")
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

my_dog = Dog("Axel", 8)
my_dog.bark()
my_dog.display_info()