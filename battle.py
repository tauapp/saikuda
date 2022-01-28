from creature import Creature
from fightable import Fightable
import util_io as io
from colorama import Fore, Style

class Battle:
    def __init__(self, protag: Creature, antag: Fightable):
        self.protag = protag
        self.antag=antag

    def start(self):
        io.say("The battle begins!")
        self.antag.enemy_report()
        print("")
        self.protag.report()
        while True:
            choice = self.protag.chooseAttack()
            dmg = (choice[0], max(0, choice[1] - self.antag.defense))
            #Check if the action type is attack
            if dmg[0]:
                io.say("It did " + Fore.RED + str(dmg[1]) + Style.RESET_ALL + " damage!")
            self.antag.health -= dmg[1]
            if self.antag.health <= 0:
                self.antag.health = 0
                break
            print("")
            choice = self.antag.chooseRandomAttack()
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
        else:
            print("")
            self.protag.report()
            print(Fore.RED + "You died!")