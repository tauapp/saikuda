from creature import Creature
from fightable import Fightable
from player import Player
import util_io as io
from _colorama import Fore, Style
import os

class Battle:
    def __init__(self, protaglist: Player, antag: Fightable):
        self.protaglist = protaglist.creatures
        self.antag=antag
        self.setProtag()

    def setProtag(self):
        lookup = [x.name for x in self.protaglist]
        start = lookup.index(io.chooseList("Choose your creature", lookup))
        self.protag = self.protaglist[start]
        self.protag.battle = self
        self.protagID = start

    def start(self):
        io.say("The battle begins!")
        os.system("clear")
        self.antag.enemy_report()
        print("")
        self.protag.report()
        while True:
            choice = self.protag.chooseAction()
            if choice[0] == 2:
                self.setProtag()
                return self.start()
            dmg = (choice[0], max(0, choice[1] - self.antag.defense))
            #Check if the action type is attack
            if dmg[0]:
                io.say("It did " + Fore.RED + str(dmg[1]) + Style.RESET_ALL + " damage!")
            self.antag.health -= dmg[1]
            if self.antag.health <= 0:
                self.antag.health = 0
                break
            print("")
            choice = self.antag.chooseRandomAction()
            dmg = (choice[0], max(0, choice[1] - self.protag.defense))
            if dmg[0]:
                io.say("It did " + Fore.RED + str(dmg[1]) + Style.RESET_ALL + " damage!")
            self.protag.health -= dmg[1]
            if self.protag.health <= 0:
                self.protag.health = 0
                break
            os.system("clear")
            print("")
            self.antag.enemy_report()
            print("")
            self.protag.report()
        if self.antag.health <= 0:
            print("")
            self.antag.enemy_report()
            print(Fore.GREEN +"You win!")
            return True
        else:
            print("")
            self.protag.report()
            print(Fore.RED + self.protag.name + " died!")
            os.system("clear")
            self.protaglist.pop(self.protagID)
            if self.protag.name != "You":
                self.setProtag()
                self.start()
            else:
                return False
