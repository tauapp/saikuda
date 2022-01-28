from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle

init(autoreset = True)

player = Creature("You", 500, 100, 10, 5, [
  Attack(
    "Beam",
    5,
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
])

animal = Fightable("Bear", 1000, 100, 20, 10, [
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