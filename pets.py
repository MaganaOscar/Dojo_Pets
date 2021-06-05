class Pet:
    def __init__(self, name, type, tricks, health = 10, energy = 30):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.energy += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("*wheezing noise*")

class Dog(Pet):
    def __init__(self, name, type, tricks, health = 25, energy = 50):
        super().__init__(name, type, tricks, health, energy)
    def noise(self):
        print("*woof*")