from weapon import Weapon
from potion import Potion

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.manna = 100
    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_manna(self):
        return self.manna
    def suffer_damage(self, damage):
        if self.health - damage < 0:
            self.health = 0
        else: self.health -= damage
    def attack(self, opponent, weapon, is_ultimate = False):
        if self.manna >= weapon.get_cost():
            
            if is_ultimate:
                opponent.suffer_damage(weapon.ultimate_damage())
                self.manna = 0
            else:
                opponent.suffer_damage(weapon.get_damage())
                self.manna -= weapon.get_cost()
    def drink(self, potion):
        if self.health + potion.get_benefit() > 100:
            self.health = 100
        else:
            self.health += potion.get_benefit()
        potion.drink()


# p = Player("John")
# print(p.get_name())
# print(p.get_health())
# print(p.get_manna())
