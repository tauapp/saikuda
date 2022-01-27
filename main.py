from colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack

init(autoreset = True)

player = Creature("Animal", 100, 100, 0, 5, [
  Attack(
    "Tackle",
    10,
    30
  )
])
player.report()