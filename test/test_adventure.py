# This file is used to test your code
# Don't change it

from player import Player
from weapon import Weapon
from blaster import Blaster
from sword import Sword
from potion import Potion
from magicelixir import MagicElixir

def test_create():
    p = Player("Saruman")
    assert p.get_name() == "Saruman"
    assert p.get_health() == 100
    assert p.get_manna() == 100

def test_potion():
    po = Potion("Mandrake")
    assert po.get_name() == "Mandrake"
    assert po.get_benefit() == 10
    e = MagicElixir()
    assert e.get_name() == "MagicElixir"
    assert e.get_benefit() == 20

def test_weapon():
    w = Weapon("Rock")
    assert w.get_name() == "Rock"
    assert w.get_damage() == 0
    assert w.get_cost() == 0

def test_sword_and_blaster():
    s = Sword()
    assert s.get_name() == "Sword"
    assert s.get_damage() == 5
    assert s.get_cost() == 5
    assert s.ultimate_damage() == 50
    b = Blaster()
    assert b.get_name() == "Blaster"
    assert b.get_damage() == 10
    assert b.get_cost() == 2
    assert b.ultimate_damage() == 15

def test_weapon_causes_damage():
    frodo = Player("Frodo")
    sauron = Player("Sauron")
    s = Sword()
    sauron.attack(frodo, s)
    assert sauron.get_health() == 100
    assert sauron.get_manna() == 95
    assert frodo.get_health() == 95
    assert frodo.get_manna() == 100

def test_drink_elixir():
    e = MagicElixir()
    assert e.get_benefit() == 20
    e.drink()
    assert e.get_benefit() == 0

def test_health_restored():
    frodo = Player("Frodo")
    sauron = Player("Sauron")
    s = Sword()
    for _ in range(5):
        sauron.attack(frodo, s)
    assert frodo.get_health() == 75
    e = Potion("Catswort", benefit=7)
    frodo.drink(e)
    assert frodo.get_health() == 82

def test_health_bounds():
    frodo = Player("Frodo")
    frodo.suffer_damage(200)
    assert frodo.get_health() == 0
    sauron = Player("Sauron")
    s = Sword()
    for _ in range(25):
        frodo.attack(sauron, s)
    assert sauron.get_health() == 0
    assert frodo.get_manna() == 0
