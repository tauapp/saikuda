from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle
from item import Item

init(autoreset = True)



#Shared item list making use of Python's Pass-by-reference
items = [
  Item(
    "Donut",
    100,
    250
  ),
  Item(
    "Steak",
    2500,
    100
  )
]

players = [Creature("You", 10000, 1000, 750, 50, [
  Attack(
    "Beam",
    10,
    5
  ),
  Attack(
    "Energy Ball",
    50,
    100
  ),
  Attack(
    "Plasma Beam",
    100,
    250
  )
], items),
Creature("Cat", 5000, 500, 50, 50, [
  Attack(
    "Scratch",
    10,
    5
  ),
  Attack(
    "Flurry",
    50,
    40
  ),
  Attack(
    "Nine Lives",
    500,
    500
  )
], items)]

animal = Fightable("Bear", 50000, 1000, 300, 100, [
  Attack(
    "Scratch",
    10,
    5
  ),
  Attack(
    "Crushing Swipe",
    40,
    250
  )
] , [])

battle = Battle(players, animal)
battle.start()