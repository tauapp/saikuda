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
import os.path
import pickle

init(autoreset = True)
io.clear()

def createNewGame():
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
    attack = 20,
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
      {"exp": 25, "energy": 5, "defense": 1, "attack": 2, "health": 5},
      {"exp": 75, "energy": 5, "defense": 1, "attack": 2, "health": 5},
      {"exp": 150, "energy": 6, "defense": 2, "attack": 3, "health": 6},
      {"exp": 250, "energy": 6, "defense": 2, "attack": 3, "health": 6},
      {"exp": 400, "energy": 7, "defense": 3, "attack": 4, "health": 7},
      {"exp": 600, "energy": 7, "defense": 3, "attack": 4, "health": 7},
      {"exp": 900, "energy": 8, "defense": 4, "attack": 5, "health": 8},
    ]
  )

  player = Player(
    name=name,
    creatures=[you],
    items=[

    ]
  )

  #Tracks the player's area
  player.state["area"] = "mountain"
  start.create(player).start()

#Checks if a save file already exists. If it does, load it.
def main():
  if os.path.isfile("saves/save.pickle"):
    try:
      savefile = pickle.load(open("saves/save.pickle", "rb"))
    except:
      io.say("It seems like the save file is corrupted.")
      io.say("Starting a new game...")
      return createNewGame()

    io.say("Loading from save file...")
    io.narr("Welcome back to Saikuda!")
    return savefile.start()
    
  else:
    return createNewGame()

main()


