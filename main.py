from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle

init(autoreset = True)

player = Creature("You", 100, 100, 0, 5, [
  Attack(
    "Tackle",
    10,
    30
  )
])

animal = Fightable("Bear", 100, 100, 0, 5, [
  Attack(
    "Scratch",
    10,
    30
  )
])

battle = Battle(player, animal)
battle.start()