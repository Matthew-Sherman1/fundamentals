class Pet:
    def __init__(self, name, types, tricks, health,energy):
        self.name = name
        self.types = types
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep (self):
        self.energy += 50
        print("Im sleeeepy", "Health:", self.health, "Energy:", self.energy)
        return self
    def eat (self):
        if self.health and self.energy > 100:
            self.health = 100
            self.energy = 100
            print('im not hungry', "Health:", self.health, "Energy:", self.energy)
        else:
            self.health += 15
            self.energy += 15
            print("Im so full", "Health:", self.health, "Energy:", self.energy)
        return self
    def play(self):
        self.health -=5
        self.energy -= 10
        print("thanks for throwing the ball", "Health:", self.health, "Energy:", self.energy)
        return self
    def noise (self):
        print('WOOF! WOOF! Thanks for the bath')
        return self