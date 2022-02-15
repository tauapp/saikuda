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
os.system("clear")
io.say(Fore.GREEN + Style.BRIGHT  + "Welcome To Saikuda!")
io.narr("When you see a sentence starting with " + Fore.GREEN + Style.BRIGHT + "~" + Style.RESET_ALL + ", press Enter to continue.")
io.narr("Before you start the game, please enter a name. (Press [Enter] to continue)")
io.narr("I know it may be tempting, but do not choose a joke name. It'll get old really quickly.")

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
      req = 0,
      speed = 0.05
    )
  ],
  level = 0,
  exp = 0,
  leveltable = [
    {"exp": 0, "energy": 20, "defense": 1, "attack": 5, "health": 20},
    {"exp": 10, "energy": 30, "defense": 5, "attack": 7, "health": 30},
    {"exp": 20, "energy": 40, "defense": 10, "attack": 10, "health": 40},
    {"exp": 30, "energy": 50, "defense": 15, "attack": 15, "health": 50},
    {"exp": 40, "energy": 60, "defense": 20, "attack": 20, "health": 60},
    {"exp": 50, "energy": 70, "defense": 25, "attack": 25, "health": 70},
    {"exp": 60, "energy": 80, "defense": 30, "attack": 30, "health": 80},
    {"exp": 70, "energy": 90, "defense": 35, "attack": 35, "health": 90},
    {"exp": 80, "energy": 100, "defense": 40, "attack": 40, "health": 100},
  ]
)

player = Player(
  name=name,
  creatures=[you],
  items=[
    Item(
      "Chocolate",
      5,
      5
    )
  ]
)
os.system("clear")
start.create(player).start()