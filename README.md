# Compleat Adventure

This homework models an adventure game, with players, potions, treasures and weapons. You'll be writing several different classes to represent all these objects.

You will write and submit multiple python files, one for each class. Every class that you create is a separate file, e.g. if you write a Player class, create **player.py**. If you create another file that wants to use the Player class, add this line to the top:
```
from player import Player
```
This tells Python to import the Player class from the file player.py.

## Superclasses
### Task 1

Create a `Player` class, that represents a player. Put this in **player.py**.

Every Player has a name (String), and a health level (integer), and a manna level (integer). The health affects if you stay alive in the game, and the manna level affects how much you can wield a weapon to attack other players.
- Create a constructor for Player that takes a String for the name, and initializes the health to 100 and manna to 100.
- Create getters for the name (`get_name()`) and health (`get_health()`) and manna (`get_manna()`)

### Task 2

Create a `Potion` class that represents a potion. Drinking a potion restores a Player's health. Put this in **potion.py**.

Every Potion has a name, and a benefit level (int), representing how many points it restores to a Player if the potion is drunk.
- Create a constructor for Potion that takes a String name, and and a benefit level, and initializes the name and benefit level for that potion. If the benefit level is not specified, the default value is 10 (read about default arguments [here](https://www.geeksforgeeks.org/default-arguments-in-python/)).
- Create a getter (`get_name`) that returns the name of the potion.
- Create a getter (`get_benefit`) that returns the benefit level of the potion. 
- Create a `drink` method that
  - Returns the value of the benefit level of the potion, and
  - Reduces the benefit value of the potion to 0 (after you drink a potion, it loses all potency).

### Task 3

Create a `Weapon` class that represents a weapon. Getting hit by a weapon causes a reduction in the Player's health. Using a weapon reduces the Player's manna. Put this in **weapon.py**.

Every Weapon has a name, and a damage level (int), representing how many points it reduces a Player's health if the Player is hit by it, and a cost to using it (int).
- Create a constructor for Weapon that takes a String name of the weapon. It initializes the damage level to 0, and the cost to 0.
- Create a getter (`get_damage`) that returns the damage level of the weapon.
- Create a getter (`get_name`) that returns the name of the weapon.
- Create a getter (`get_cost`) that returns the cost of using the weapon.

Every weapon has a special ultimate level move that inflicts lots of damage, but costs all the player's manna to use.

- Create a method `ultimate_damage` that returns the amount of damage the weapon would cause if the ultimate move was used. This should just return 0 for the Weapon superclass.

## Subclasses

### Task 4

Create an `MagicElixir` class that is a subclass of Potion. MagicalElixirs are powerful and have twice the benefit of standard Potions. Put this in **magicelixir.py**.

- Create a constructor for MagicElixir that takes no arguments, and sets the name of the Potion to "MagicElixir", and initializes the benefit to 20.

### Task 5

Create a `Sword` subclass of Weapon. Put this in **sword.py**.

- Swords inflict 5 damage points and cost 5 points in manna.
- Create a constructor for Sword that takes no arguments, and initializes the damage level to 5, the cost to 5, and the name to "Sword".
- The ultimate move for a Sword causes 50 points of damage. Write the `ultimate_damage` function for Sword to return the amount of ultimate damage.

Create a `Blaster` subclass of Weapon. Put this in **blaster.py**.

- Blasters inflict 10 damage points and cost 2 points to use.
- Create a constructor for Blaster that takes no arguments, and intializes the damage level to 10, the cost to 2, and the name to "Blaster".
- The ultimate move for Blaster causes 15 points of damage. Write the `ultimate_damage` function for Blaster to return the amount of ultimate damage.


### Task 6

Players can attack each other with weapons. When a Player is attacked, the player suffers damage.

- Write a void method `suffer_damage` in the Player class. When this method is called on a player, the player's health points are reduced by the given amount of damage. Damage never goes below 0.
```
def suffer_damage(self, damage):
    """The player's health is reduced by damage points."""
    ....
```

Write a method in the Player class called `attack()`. Attack takes three arguments:
- an opponent to attack,
- a weapon to attack the opponent with,
- a boolean is_ultimate, specifying whether this is an ultimate attack. The default value of this argument should be False. 
- This means that you can call suffer_damage method without the is_ultimate argument, in which case it is set to False by default. Read about default arguments [here](https://www.geeksforgeeks.org/default-arguments-in-python/).
The attack method should reduce the opponent's health level by the weapon's damage amount. This method should use the suffer_damage method you wrote earlier.
- Make sure you have enough manna to attack. You must have at least the weapon's cost in manna to do any damage. Without sufficient manna, the attack produces no damage in your opponent. The Player's manna is reduced by the cost of using the weapon. If it is an ultimate move, the Player's manna is reduced to 0.
```
def attack(self, opponent, weapon, is_ultimate=False):
  """Attack the opponent with the weapon."""
  ...
```

### Task 7

Players can restore their health by drinking potions.

Write a Player method drink() that takes a Potion as an argument. It should increase the Player's health points by the potion's benefit. However, the maximum health of a Player is 100 and cannot increase beyond that.
```
def drink(self, potion):
  """Drinking the potion improves the player's health.
   The potion's benefit is completely depleted.
  """
  ...
```
Note that there are two methods named "drink".  The Player.drink method is not the same as the Potion.drink method.

### Task 8

Write a main program in the file **adventure.py** that has gameplay that exactly goes like this. Copy this main program. Does the game play run the way you expect? If not, fix your code till it does what it should.
```
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
```




## Submitting

Submit all your files: player.py potion.py magicelixir.py weapon.py sword.py blaster.py adventure.py

# Hints
Remember that all methods in a class start with the `self` as the first parameter.


# What's in a name?

The name of this homework is a homage to an early adventure game that I used to love as a kid. I spent hours playing this game, and in fact completed it all the way to the end.
