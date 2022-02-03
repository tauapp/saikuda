import os

from player import Player
try:
  __import__('_colorama')
except:
  print("Configuring...")
  os.system("pip install colorama")
  os.system("pip install inquirer")
  os.system("clear")

from _colorama import init, Fore, Back, Style
import util_io as io
from creature import Creature
from attack import Attack
from fightable import Fightable
from battle import Battle
from item import Item
import time

init(autoreset = True)
io.narr(Fore.GREEN + Style.BRIGHT  + "Welcome To Saikuda!")
tutorial = io.chooseList("Do you want to go through the tutorial?", ["Yes", "No"])
if tutorial == "Yes":
  io.narr("In the world of Saikuda, you will have many challenges, and one of those challenges is unfriendly creatures.")
  io.narr("When you start a battle, you can choose one of your creatures to fight for you, or you can go fight yourself.")
  io.narr("You often have more health and defense than your creatures, but they have more powerful attacks.")
  io.narr("When it's your creature's turn to battle, they have multiple choices:")
  io.narr("To fight, defend, use an item, rest, or switch creature.")
  io.narr("When you fight, you will see your list of attacks in a format like this:")
  io.narr("> Tackle "+ Fore.RED + "10" + Style.RESET_ALL + "/" + Fore.BLUE + "5")
  io.narr("The 10/5 means that this attack has an intensity of 10 and costs 5 energy to perform.")
  io.narr("Intensity is used to calculate the amount of damage an attack does.")
  io.narr("It takes energy to perform an attack. If you don't have enough energy to do an attack, you can try, but it won't do any damage.")
  io.narr("Next is defending. Defending triples your DEFENSE statistic, allowing you to take less damage from attacks.")
  io.narr("Next is choosing Items. If you choose an Item, you can consume it, restoring some of your health and energy. Items are in the format:")
  io.narr("> Cake "+ Fore.RED + "100" + Style.RESET_ALL + "/" + Fore.BLUE + "200")
  io.narr("The 100/200 means the cake heals 100 health and 200 energy.")
  io.narr("Resting will replenish 20% of your maximum energy.")
  io.narr("Switching creatures does exactly what is seems like. Switching creatures in the middle of a battle is important in the future RPG because once you lose a creature, it's gone forever.")
  io.narr("Remember: If one of your creatures dies, you can switch to another, but if you die, the game ends.")
  io.narr("Hopefully that wasn't too long. Now for the battle!")

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

creatures = [Creature("You", 10000, 1000, 750, 50, [
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
], items, 1, 0, []),
Creature("Cat", 5000, 500, 500, 50, [
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
], items, 1, 0, [])]

animal = Fightable("Bear", 50000, 1000, 300, 100, [
  Attack(
    "Scratch",
    25,
    100
  ),
  Attack(
    "Crushing Swipe",
    40,
    250
  )
] , [], 1, 0, [])

player = Player("Main", creatures, items)

animal.conversations = [
  "You complement Bear on its sleek fur. It growls in agreement.",
  "You compliment Bear on its strength. Bear growls in agreement.",
  "You compliment Bear on its speed. Bear growls in agreement.",
  "You tell Bear that it doesn't need to fight. Bear whimpers."
]

battle = Battle(player, animal)
battle.start()
