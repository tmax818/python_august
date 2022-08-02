class Tree:
    
    def __init__(self, color, type, height):
        self.color = color
        self.type = type
        self.height = height
        print(self)

    def blow_in_wind(self):
        print(f"{self.type} tree blowing in the wind")


tree1 = Tree('green', 'maple', 50)