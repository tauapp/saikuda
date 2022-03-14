from _colorama import Fore, Style
import random
import util_io as io

def chooseRandomAction(self):
      if self.sparable:
        return (False, 0)
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