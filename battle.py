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
            dmg = abs(self.protag.chooseAttack() - self.antag.defense)
            io.say("It did " + Fore.RED + str(dmg) + Style.RESET_ALL + " damage!")
            self.antag.health -= dmg
            if self.antag.health <= 0:
                self.antag.health = 0
                break
            print("")
            dmg = abs(self.antag.chooseRandomAttack() - self.protag.defense)
            io.say("It did " + Fore.RED + str(dmg) + Style.RESET_ALL + " damage!")
            self.protag.health -= dmg
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
            print("You win!")
        else:
            print("")
            self.protag.report()
            print("You died!")