from creature import Creature
from fightable import Fightable
import util_io as io
from colorama import Fore, Style

class Battle:
    def __init__(self, protaglist: Creature, antag: Fightable):
        self.protaglist = protaglist
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
        self.antag.enemy_report()
        print("")
        self.protag.report()
        while True:
            choice = self.protag.chooseAction()
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
            print("")
            self.antag.enemy_report()
            print("")
            self.protag.report()
        if self.antag.health <= 0:
            print("")
            self.antag.enemy_report()
            print(Fore.GREEN +"You win!")
            return
        else:
            print("")
            self.protag.report()
            print(Fore.RED + self.protag.name + "died!")
            self.protaglist.pop(self.protagID)
            if self.protag.name != "You":
                self.setProtag()
                self.start()
            else:
                return