class Potion:
    def __init__(self, name, benefit = 10):
        self.name = name
        self.benefit = benefit
    def get_name(self):
        return self.name
    def get_benefit(self):
        return self.benefit
    def drink(self):
        drank = self.benefit
        self.benefit = 0
        return drank
    
# lp = Potion("Love potion #9")
# print(lp.get_name())
# print(lp.get_benefit())
# print(lp.drink())
# print(lp.get_benefit())
