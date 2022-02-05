import time
import random
from armor import Armor
import util_io as io
from _colorama import Fore, Style
from fightable import Fightable
from weapon import Weapon

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

  isCreature = True

  #Increases the player EXP at the end of the battle. If the player has leveled up, it increases their stats. Also used for currency.
  def reward(self, player, exp, money):
    pronoun = "is"
    if self.name == "You":
      pronoun = "are"
    self.exp += exp
    io.narr(self.name, "gained", exp, "EXP and", money, "aurum!")
    level = self.level
    nextlevel = level + 1
    player.aurum += money
    if self.exp >= self.leveltable[nextlevel]["exp"]:
      previousattacknumber = len(self.attack_list)
      io.narr(self.name, "leveled up!", self.name, pronoun, "now level", nextlevel, "!")
      self.attack_list = [x for x in self.possible_attacks if x.req <= nextlevel]
      if len(self.attack_list) > previousattacknumber:
        io.narr("You learned a new attack!")
      self.exp -= self.leveltable[nextlevel]["exp"]
      self.level += 1
      self.max_health += self.leveltable[nextlevel]["health"]
      self.max_energy += self.leveltable[nextlevel]["energy"]
      self.attack_str += self.leveltable[nextlevel]["attack"]
      self.defense += self.leveltable[nextlevel]["defense"]

  reduceDefense = False

  weapon = Weapon("Stick", 1)

  armor = Armor("Bandage", 1)

  battle = None

  def equipArmor(self, armor):
    self.defense /= self.armor.multiplier
    self.armor = armor
    self.defense *= self.armor.multiplier
    io.narr(self.name, "equipped the", armor.name + "!")
  
  def equipWeapon(self, weapon):
    self.attack_str /= self.weapon.multiplier
    self.weapon = weapon
    self.attack_str *= self.weapon.multiplier
    io.narr(self.name, "equipped the", weapon.name + "!")

  def chooseAction(self):

    #Formatting
    HEALTH = Fore.RED + "HEALTH" + Style.RESET_ALL
    ENERGY = Fore.BLUE + "ENERGY" + Style.RESET_ALL
    DEFENSE = Fore.GREEN + "DEFENSE" + Style.RESET_ALL

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
    choice = io.chooseList("Choose an action", [
      "Fight",
      "Talk",
      "Defend",
      "Item",
      "Rest",
      "Switch Creature",
      Fore.YELLOW + "Spare" if self.battle.antag.sparable else "Spare"
    ])
    if choice == "Fight":
      return self.chooseAttack()
    elif choice == "Talk":
      return self.talk()
    elif choice == "Defend":
      self.defense *= 3
      io.say(pronoun[0], "defended, tripling", pronoun[1] + " " + DEFENSE + "!")
      self.reduceDefense = True
      return (False, 0)
    elif choice == "Item":
      if len(self.items) == 0:
        io.say("You don't have any items!")
        return self.chooseAction()
      self.chooseItem()
      return (False, 0)
    elif choice == "Rest":
      self.energy += (self.max_energy * 0.2)
      self.energy = min(round(self.energy), self.max_energy)
      io.say(pronoun[0], "rested and recovered 20% of", pronoun[1], ENERGY + "!")
      return (False, 0)
    elif choice == "Switch Creature":
      return (2, 0)
    elif choice == "Spare" or choice == Fore.YELLOW + "Spare":
      return ("Spare", -1)
    else:
      return (False, 0)

  def talk(self):
    enemy: Fightable = self.battle.antag
    complement = random.choice(enemy.conversations)
    io.say(complement)
    time.sleep(1)
    if enemy.sparable:
      return (False, 0)
    reqpercent = float(enemy.friendship[0]) / float(enemy.friendship[1])
    initial_attack_str = enemy.attack_str / (1 - reqpercent)
    initial_defense = enemy.defense / (1 - reqpercent)
    #Set the tuple directly because tuples are immutable
    enemy.friendship = (enemy.friendship[0] + 1, enemy.friendship[1])
    reqpercent = float(enemy.friendship[0]) / float(enemy.friendship[1])
    enemy.attack_str = initial_attack_str * (1 - reqpercent)
    enemy.defense = initial_defense * (1 - reqpercent)
    if enemy.friendship[0] >= enemy.friendship[1]:
      io.say(enemy.name, "doesn't want to fight anymore. " + Fore.GREEN + "It can now be spared!")
      time.sleep(1)
      enemy.sparable = True
    return (False, 0)

    
  def chooseItem(self):
    #Formatting
    HEALTH = Fore.RED + "HEALTH" + Style.RESET_ALL
    ENERGY = Fore.BLUE + "ENERGY" + Style.RESET_ALL
    DEFENSE = Fore.GREEN + "DEFENSE" + Style.RESET_ALL
    pronoun = tuple()
    if self.name == "You":
      pronoun = ("You", "your")
    else:
      pronoun = (self.name, "its")
    lookup = [x.name for x in self.items]
    choices = [
      x.name + " " + Fore.RED + str(x.health) + Style.RESET_ALL + "/" + Fore.BLUE + str(x.energy)
      for x in self.items
    ]
    choices.insert(0, "Back")
    choice = io.chooseList("Choose an item", choices)
    if choice == "Back":
      return self.chooseAction()
    choice = lookup.index(" ".join(choice.split(" ")[:-1]))
    item = self.items[choice]
    self.health += item.health
    self.health = min(self.health, self.max_health)
    self.energy += item.energy
    self.energy = min(self.energy, self.max_energy)
    io.say(pronoun[0], "used the", item.name + ".", pronoun[0], "restored", item.health, HEALTH + " and", item.energy, ENERGY + "!")
    self.items.pop(choice)
    return

  #Choose an attack to execute
  def chooseAttack(self):
    lookup = [x.name for x in self.attack_list]
    choices = [
      x.name + " " + Fore.RED + str(x.intensity) + Style.RESET_ALL + "/" + Fore.BLUE + str(x.cost)
      for x in self.attack_list
    ]
    choices.insert(0, "Back")
    choice = io.chooseList("Choose an item", choices)
    if choice == "Back":
      return self.chooseAction()
    choice = lookup.index(" ".join(choice.split(" ")[:-1]))
    return self.attack(choice)
