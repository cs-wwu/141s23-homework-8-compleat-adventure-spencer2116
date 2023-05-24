from weapon import Weapon

class Blaster(Weapon):
    def __init__(self):
        self.name = "Blaster"
        self.damage = 10
        self.cost = 2
    def ultimate_damage(self):
        return 15
    
# dl44 = Blaster()
# print(dl44.get_cost())
# print(dl44.ultimate_damage())
