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
            io.say(self.description)
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
            print("Attack Strength:", self.player.attack_str)
            print("Defense:", self.player.defense)
            print("Health:", self.player.health)
            print("Energy:", self.player.energy)
            print("Level:", self.player.level)
            print("EXP to next level:", self.player.leveltable[self.player.level + 1]["exp"] - self.player.exp)
            print("Weapon:", self.player.weapon.name, "(Attack Multiplier:", self.player.weapon.multiplier, ")")
            print("Armor:", self.player.armor.name, "(Defense Multiplier:", self.player.armor.multiplier, ")")
            print("Aurum:", self.player.aurum)
            return self.choose()
        else:
            return self.choose()

