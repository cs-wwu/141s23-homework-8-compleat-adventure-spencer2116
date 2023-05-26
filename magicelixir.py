from potion import Potion

class MagicElixir(Potion):
    def __init__(self):
        self.name = "MagicElixir"
        self.benefit = 20


# lp10 = MagicElixir()
# print(lp10.get_benefit())
# print(lp10.get_name())