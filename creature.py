import util_io as io
from colorama import Fore
from fightable import Fightable

class Creature(Fightable):
  def report(self):
    io.progressBar('HP',
      stat = self.health,
      max = self.max_health,
      color_inner = Fore.RED,
      color_outer = Fore.GREEN
    )

    io.progressBar('Energy',
      stat = self.energy,
      max = self.max_energy,
      color_inner = Fore.BLUE,
      color_outer = Fore.GREEN
    )

  #Choose an attack to execute
  def chooseAttack(self):
    lookup = [x.name for x in self.attack_list]
    choices = [
      x.name + " " + Fore.RED + str(x.intensity) + Fore.WHITE + "/" + Fore.BLUE + str(x.cost)
      for x in self.attack_list
    ]
    choice = " ".join(io.chooseList("Choose an attack!", choices).split(" ")[:-1])
    return self.attack(lookup.index(choice))
