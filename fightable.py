import util_io as io
from colorama import Fore, Style
import random

class Fightable:

    name = ""

    health = 100

    max_health = 100

    defense = 0

    attack_str = 5

    attack_list = []

    energy = 100

    max_energy = 100

    items = []

    #The current battle
    battle = None

    #Perform an Attack and deduct from energy
    def attack(self, index):
      #Attack being done
      att = self.attack_list[index]
      if att.cost > self.energy:
        pronoun = "it was" if self.name != "You" else "you were"
        io.say(self.name, "tried to attack, but", pronoun, "too tired!")
        return (False, 0)
      self.energy -= att.cost
      io.say(self.name, "used", Fore.GREEN + att.name + Style.RESET_ALL + "!")
      return (True, att.intensity * self.attack_str)

    def chooseRandomAction(self):
      #Formatting
      HEALTH = Fore.RED + "HEALTH" + Style.RESET_ALL
      ENERGY = Fore.BLUE + "ENERGY" + Style.RESET_ALL
      DEFENSE = Fore.GREEN + "DEFENSE" + Style.RESET_ALL
      att = random.randint(0, len(self.attack_list) - 1)
      cost = self.attack_list[att].cost
      if cost > self.energy:
        self.energy += (self.max_energy * 0.2)
        self.energy = min(round(self.energy), self.max_energy)
        io.say(self.name + " rested and recovered 20% of its", ENERGY + "!")
        return (False, 0)
      return self.attack(att)

    def enemy_report(self):
      io.progressBar('Enemy HP',
      stat = self.health,
      max = self.max_health,
      color_inner = Fore.GREEN,
    )

    def __init__(self, name, max_health, max_energy, defense, attack, attack_list, items):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.defense = defense
        self.attack_str = attack
        self.attack_list = attack_list
        self.energy = max_energy
        self.max_energy = max_energy
        self.items = items