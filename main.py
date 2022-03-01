import os

try:
  __import__('colorama')
  __import__('inquirer')
  __import__('blessed')
except:
  print("Configuring...")
  os.system("pip install colorama")
  os.system("pip install inquirer")
  os.system("pip install blessed")
  os.system("clear")

from player import Player
from _colorama import init, Fore, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle
from item import Item
import time
import rooms.mountain.start as start

init(autoreset = True)
io.clear()
io.say(Fore.GREEN + Style.BRIGHT  + "Welcome To Saikuda!")
io.narr("When you see a sentence starting with " + Fore.GREEN + Style.BRIGHT + "~" + Style.RESET_ALL + ", press Enter to continue.")
io.narr("Before you start the game, please enter a name. (Press [Enter] to continue)")

name = io.ask("Enter a name")

you = Creature(
  name = "You",
  max_health = 20,
  max_energy = 20,
  defense = 1,
  attack = 5,
  attack_list = [
    Attack(
      name = "Punch",
      intensity= 1,
      cost = 5,
      speed = 0.05
    )
  ],
  level = 0,
  exp = 0,
  leveltable = [
    dict(),
    {"exp": 10, "energy": 5, "defense": 5, "attack": 2, "health": 5},
    {"exp": 20, "energy": 7, "defense": 7, "attack": 5, "health": 7},
    {"exp": 30, "energy": 15, "defense": 15, "attack": 15, "health": 15},
    {"exp": 40, "energy": 20, "defense": 20, "attack": 20, "health": 20},
    {"exp": 50, "energy": 30, "defense": 30, "attack": 30, "health": 30},
    {"exp": 60, "energy": 50, "defense": 50, "attack": 50, "health": 50},
    {"exp": 70, "energy": 80, "defense": 80, "attack": 80, "health": 80},
    {"exp": 80, "energy": 100, "defense": 100, "attack": 100, "health": 100},
  ]
)

player = Player(
  name=name,
  creatures=[you],
  items=[

  ]
)
io.clear()
start.create(player).start()