class Dojo:
    
    def __init__(self, location) -> None:
        self.location = location
        self.ninjas = []

    def add_ninja(self, ninja):
        self.ninjas.append(ninja)

    

class Ninja:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

ninja1 = Ninja('Nisrine', 31)
ninja2 = Ninja('Tre', 27)

dojo1 = Dojo('burbank')
dojo2 = Dojo('san jose')