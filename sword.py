from weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.damage = 5
        self.cost = 5
    def ultimate_damage(self):
        return 50
    
# anduril = Sword()
# print(anduril.get_cost())
# print(anduril.ultimate_damage())