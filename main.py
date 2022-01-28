from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle
from item import Item

init(autoreset = True)

player = Creature("You", 10000, 1000, 100, 50, [
  Attack(
    "Beam",
    1,
    5
  ),
  Attack(
    "Energy Ball",
    10,
    20
  ),
  Attack(
    "Plasma Beam",
    100,
    75
  )
], [
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
])

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
])

battle = Battle(player, animal)
battle.start()