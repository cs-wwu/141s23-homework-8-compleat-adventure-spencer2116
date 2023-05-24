from player import Player
from sword import Sword
from blaster import Blaster
from magicelixir import MagicElixir


# create two players
frodo = Player("Frodo")
sauron = Player("Sauron")

# Create a magical elixir
elixir = MagicElixir()

# Create some weapons
sting = Sword()
blaster = Blaster()

# Play the game! -- the players take turns attacking each other
sauron.attack(frodo, blaster)   # Sauron attacks Frodo with a blaster
frodo.attack(sauron, sting);     # Frodo attacks Sauron with his sword Sting
sauron.attack(frodo, blaster)   # Sauron blasts Frodo again
sauron.attack(frodo, blaster, is_ultimate=True)   # Sauron ultimates
sauron.attack(frodo, blaster)   # desperation move

# Frodo drinks a potion
frodo.drink(elixir)

# Let's examine who's healthier
print("Frodo's health: %d, manna: %d" % (frodo.get_health(), frodo.get_manna()))
print("Sauron's health: %d, manna: %d" % (sauron.get_health(), sauron.get_manna()))