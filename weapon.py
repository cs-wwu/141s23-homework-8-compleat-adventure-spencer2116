class Weapon:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.cost = 0
    def get_damage(self):
        return self.damage
    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def ultimate_damage(self):
        return 0
    
# myAxe = Weapon("And-my-Axe")
# print(myAxe.get_name())
# print(myAxe.get_cost())
# print(myAxe.get_damage())
# print(myAxe.ultimate_damage())
