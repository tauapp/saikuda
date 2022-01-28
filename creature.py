import util_io as io
from colorama import Fore, Style
from fightable import Fightable

class Creature(Fightable):
  def report(self):
    io.progressBar('HP',
      stat = self.health,
      max = self.max_health,
      color_inner = Fore.RED,
    )

    io.progressBar('Energy',
      stat = self.energy,
      max = self.max_energy,
      color_inner = Fore.BLUE,
    )

  reduceDefense = False

  def chooseAction(self):

    #If the user defended last round, remove the defense
    if self.reduceDefense:
      self.defense /= 3
      self.defense = round(self.defense)
      self.reduceDefense = False

    pronoun = tuple()
    if self.name == "You":
      pronoun = ("You", "your")
    else:
      pronoun = (self.name, "its")
    choice = io.chooseList("Choose an action:", [
      "Fight",
      "Defend",
      "Item",
      "Rest",
      "Spare"
    ])
    if choice == "Fight":
      return self.chooseAttack()
    elif choice == "Defend":
      self.defense *= 3
      io.say(pronoun[0], "defended, tripling", pronoun[1] + " " + Fore.GREEN + "DEFENSE" + Style.RESET_ALL + "!")
      self.reduceDefense = True
      return (False, 0)
    elif choice == "Item":
      self.chooseItem()
      return (False, 0)
    elif choice == "Rest":
      self.energy += (self.max_energy * 0.2)
      self.energy = min(round(self.energy), self.max_energy)
      io.say(pronoun[0], "rested and recovered 20% of", pronoun[1], "energy!")
      return (False, 0)
    else:
      #TODO
      io.say("The enemy doesn't want to be spared!")
      return (False, 0)
    
  def chooseItem(self):
    lookup = [x.name for x in self.items]
    choices = [
      x.name + " " + Fore.RED + str(x.health) + Style.RESET_ALL + "/" + Fore.BLUE + str(x.energy)
      for x in self.items
    ]
    choice = lookup.index(" ".join(io.chooseList("Choose an item", choices).split(" ")[:-1]))
    item = self.items[choice]
    self.health += item.health
    self.health = min(self.health, self.max_health)
    self.energy += item.energy
    self.energy = min(self.energy, self.max_energy)
    io.say("You used the", item.name + ".", "You restored", item.health, "health and", item.energy, "energy!")
    self.items.pop(choice)
    return

  #Choose an attack to execute
  def chooseAttack(self):
    lookup = [x.name for x in self.attack_list]
    choices = [
      x.name + " " + Fore.RED + str(x.intensity) + Style.RESET_ALL + "/" + Fore.BLUE + str(x.cost)
      for x in self.attack_list
    ]
    choice = " ".join(io.chooseList("Choose an attack", choices).split(" ")[:-1])
    return self.attack(lookup.index(choice))
