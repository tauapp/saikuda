import os
from battle import Battle
import util_io as io
import random

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
        choices = [("Check Stats", )]
        if self.exits != {}:
            choices.append(("Move", ))
        if self.actions != []:
            #Merge actions and choices list
            choices.extend(self.actions)
        choice = io.chooseList("What do you want to do?", [x[0] for x in choices])
        if choice == "Move":
            room = self.exits[io.chooseList("Where do you want to go?", self.exits.keys())]
            return room.start()
        elif choice == "Check Stats":
            io.clear()
            player = self.player.creatures[0]
            print("\nAttack Strength:", player.attack_str)
            print("Defense:", player.defense)
            print("Health:", player.health)
            print("Energy:", player.energy)
            print("Level:", player.level)
            print("EXP to next level:", player.leveltable[player.level + 1]["exp"] - player.exp)
            print("Weapon:", player.weapon.name, "( Attack Multiplier:", player.weapon.multiplier, ")")
            print("Armor:", player.armor.name, "( Defense Multiplier:", player.armor.multiplier, ")")
            print("Aurum:", self.player.aurum)
            input("\nPress enter to continue...")
            return self.choose()
        else:
            chosen = [x for x in self.actions if x[0] == choice][0]
            chosen[1](self.player)
            return self.choose()

