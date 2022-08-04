
class Parent:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass

    def give_orders(self):
        print("Go to your room")


class Child(Parent):
    
    def __init__(self, name, age, potty_trained = False) -> None:
        super().__init__(name, age)
        self.potty_trained = pottyasdf
    
johnny = Child("Johnny", 9)


class Animal:

    def __init__(self, gender, name) -> None:
        self.gender = gender
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass