import util_io as io
from colorama import Fore

class Fightable:

    name = ""

    health = 100

    max_health = 100

    defense = 0

    attack_str = 5

    attack_list = []

    energy = 100

    max_energy = 100

    def attack(self, index):
      #Attack being done
      att = self.attack_list[index]
      self.energy -= att.cost
      io.say(self.name, "performed", att.name + "!")
      return att.intensity * self.attack_str

    def chooseAttack(self):
      lookup = [x.name for x in self.attack_list]
      choices = [
        x.name + " " + Fore.RED + str(x.intensity) + Fore.WHITE + "/" + Fore.BLUE + str(x.cost)
        for x in self.attack_list
      ]
      choice = " ".join(io.chooseList("Choose an attack!", choices).split(" ")[:-1])
      return lookup.index(choice)

    def __init__(self, name, max_health, max_energy, defense, attack, attack_list):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.defense = defense
        self.attack_str = attack
        self.attack_list = attack_list
        self.energy = max_energy
        self.max_energy = max_energy