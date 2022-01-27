import util_io as io
from colorama import Fore
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

    #Perform an Attack and deduct from energy
    def attack(self, index):
      #Attack being done
      att = self.attack_list[index]
      if att.cost > self.energy:
        io.say(self.name, "tried to attack, but it was too tired!")
        return 0
      self.energy -= att.cost
      io.say(self.name, "used", att.name + "!")
      return att.intensity * self.attack_str

    def chooseRandomAttack(self):
      att = random.randint(0, len(self.attack_list) - 1)
      self.attack(att)
      return self.attack_list[att].intensity * self.attack_str

    def __init__(self, name, max_health, max_energy, defense, attack, attack_list):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.defense = defense
        self.attack_str = attack
        self.attack_list = attack_list
        self.energy = max_energy
        self.max_energy = max_energy