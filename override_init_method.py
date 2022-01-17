class Dinosaur:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight


class Carnivore:
    def __init__(self, diet):
        self.diet = diet


class Tyrannosaurus (Dinosaur, Carnivore):
    def __init__(self, size, weight, diet):
        Dinosaur.__init__ (self, size, weight)
        Carnivore.__init__ (self, diet)


tiny = Tyrannosaurus (12, 14, "whatever it wants")
print(tiny.diet)