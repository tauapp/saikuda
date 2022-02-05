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

    def __init__(self, map, player, actions = lambda: None, enemychance = 0, description = "", exits = {}):
        self.map = map
        self.enemychance = enemychance
        self.description = description
        self.actions = actions
        self.exits = exits
        self.player = player

    def start(self):
        print(self.map + "\n")
        if self.description != None:
            io.narr(self.description)
        if self.enemychance >= random.random():
            io.narr("A wild " + self.enemy.name + " appears!")
            #Start battle between player and enemy
            if Battle(self.player, self.enemy).start() == False:
                #TODO: Go back to previous room
                pass
        #Run any custom actions provided for the room
        self.actions()
        self.choose()

    def choose(self):
        choice = io.chooseList("What do you want to do?", [
            "Move",
            "Check Stats"
        ])
        if choice == "Move":
            room = self.exits[io.chooseList("Where do you want to go?", self.exits.keys())]
            return room.start()
        elif choice == "Check Stats":
            os.system("clear")
            player = self.player.creatures[0]
            print("Attack Strength:", player.attack_str)
            print("Defense:", player.defense)
            print("Health:", player.health)
            print("Energy:", player.energy)
            print("Level:", player.level)
            print("EXP to next level:", player.leveltable[player.level + 1]["exp"] - player.exp)
            print("Weapon:", player.weapon.name, "( Attack Multiplier:", player.weapon.multiplier, ")")
            print("Armor:", player.armor.name, "( Defense Multiplier:", player.armor.multiplier, ")")
            print("Aurum:", self.player.aurum)
            return self.choose()
        else:
            return self.choose()

