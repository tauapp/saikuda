from creature import Creature
from fightable import Fightable
import util_io as io

class Battle:
    def __init__(self, protag: Creature, antag: Fightable):
        self.protag = protag
        self.antag=antag

    def start(self):
        io.say("The battle begins!")
        while self.protag.health > 0 and self.antag.health > 0:
            dmg = abs(self.protag.chooseAttack() - self.antag.defense)
            io.say("It did", dmg, "damage!")
            self.antag.health -= dmg
            print("")
            dmg = abs(self.antag.chooseRandomAttack() - self.protag.defense)
            io.say("It did", dmg, "damage!")
            self.protag.health -= dmg
            print("")
            self.protag.report()