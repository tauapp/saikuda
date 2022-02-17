import os
from battle import Battle
import util_io as io
import random
from _colorama import Fore, Style

class Room:

    exits = {
        "North": None,
        "South": None,
        "East": None,
        "West": None,
    }

    def __init__(self, map, player, scripts = lambda x: None, enemychance = 0, exits = {}, actions = []):
        self.map = map
        self.enemychance = enemychance
        self.scripts = scripts
        self.exits = exits
        self.player = player
        #Each action is a tuple with a name and a function
        self.actions = actions

    def start(self):
        io.clear()
        print(self.map + "\n")
        #Run any custom actions provided for the room
        self.scripts(self.player)
        if self.enemychance >= random.random():
            pass
        self.choose()

    def choose(self):
        io.clear()
        choices = [("Check stats", )]
        if self.exits != {}:
            choices.insert(0, ("Move", ))
        if self.actions != []:
            #Merge actions and choices list
            choices.extend(self.actions)
        choice = io.chooseList("What do you want to do?", [x[0] for x in choices])
        if choice == "Move":
            room = self.exits[io.chooseList("Where do you want to go?", self.exits.keys())]
            return room.start()
        elif choice == "Check stats":
            io.clear()
            player = self.player.creatures[0]
            print(f"\n{Fore.RED}Attack Strength:{Style.RESET_ALL}", int(player.attack_str))
            print(f"{Fore.GREEN}Defense:{Style.RESET_ALL}", int(player.defense))
            print(f"{Fore.RED}Health:{Style.RESET_ALL} {int(player.health)}/{player.max_health}")
            print(f"{Fore.BLUE}Energy:{Style.RESET_ALL} {int(player.energy)}/{player.max_energy}")
            print(f"{Fore.YELLOW}Level:{Style.RESET_ALL}", int(player.level))
            print(f"{Fore.YELLOW}EXP to next level:{Style.RESET_ALL}", player.leveltable[player.level + 1]["exp"] - player.exp)
            print(f"{Fore.RED}Weapon:{Style.RESET_ALL}", player.weapon.name, "( Attack Multiplier:", player.weapon.multiplier, ")")
            print(f"{Fore.BLUE}Armor:{Style.RESET_ALL}", player.armor.name, "( Defense Multiplier:", player.armor.multiplier, ")")
            print(f"{Fore.YELLOW}Aurum:{Style.RESET_ALL}", int(self.player.aurum))
            input(f"\nPress enter to continue...")
            return self.choose()
        else:
            chosen = [x for x in self.actions if x[0] == choice][0]
            chosen[1](self.player)
            return self.choose()

