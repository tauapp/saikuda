import util_io as io
from colorama import Fore
from fightable import Fightable

class Creature(Fightable):
  def report(self):
    io.progressBar('HP',
      stat = self.health,
      max = self.max_health,
      color_inner = Fore.RED,
      color_outer = Fore.GREEN,
      color_contrast = Fore.LIGHTRED_EX
    )

    io.progressBar('Energy',
      stat = self.health,
      max = self.max_health,
      color_inner = Fore.LIGHTGREEN_EX,
      color_outer = Fore.BLUE,
      color_contrast = Fore.GREEN
    )
