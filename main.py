from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle
from item import Item

init(autoreset = True)

items = [
  Item(
    "Donut",
    50,
    50
  ),
  Item(
    "Donut",
    50,
    50
  )
]

players = [Creature("You", 10000, 1000, 100, 50, [
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
Creature("Cat", 5000, 500, 50, 100, [
  Attack(
    "Scratch",
    10,
    5
  ),
  Attack(
    "Flurry",
    50,
    50
  ),
  Attack(
    "Nine Lives",
    500,
    500
  )
], items)]

animal = Fightable("Bear", 100000, 100, 100, 25, [
  Attack(
    "Scratch",
    10,
    5
  ),
  Attack(
    "Crushing Swipe",
    40,
    25
  )
] , [])

battle = Battle(players, animal)
battle.start()