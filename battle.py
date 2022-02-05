from creature import Creature
from fightable import Fightable
from player import Player
import util_io as io
from _colorama import Fore, Style
import os

class Battle:
    def __init__(self, player: Player, antag: Fightable):
        self.player = player
        self.protaglist = player.creatures
        self.antag=antag
        self.setProtag()

    def setProtag(self):
        lookup = [x.name for x in self.protaglist]
        if len(lookup) == 1:
            start = 0
            self.protag = self.protaglist[start]
            self.protag.battle = self
            self.protagID = start
            return
        start = lookup.index(io.chooseList("Choose your creature", lookup))
        self.protag = self.protaglist[start]
        self.protag.battle = self
        self.protagID = start

    def start(self):
        io.say("The battle begins!")
        os.system("clear")
        self.antag.chooseDialogue()
        self.antag.enemy_report()
        print("")
        self.protag.report()
        while True:
            choice = self.protag.chooseAction()
            if choice[0] == 2:
                self.setProtag()
                return self.start()
            dmg = (choice[0], max(0, choice[1] - self.antag.defense))
            #Check if the character betrayed the enemy
            if self.antag.sparable and dmg[0] == True:
                io.say("It did " + Fore.RED + "999999999" + Style.RESET_ALL + " damage!")
                io.narr(Fore.RED + "It's a betrayal!")
                self.antag.health = 0
            elif dmg[0] == "Spare":
                if self.antag.sparable:
                    io.narr(Fore.GREEN + self.antag.name, "was spared!")
                    self.protag.reward(self.player, exp = round(self.antag.max_energy / 2), money = round(self.antag.max_health / 10))
                    return True
                else:
                    io.say(Fore.RED + self.antag.name, "didn't want to be spared!")
            #Check if the action type is attack
            elif dmg[0]:
                io.say("It did " + Fore.RED + str(int(dmg[1])) + Style.RESET_ALL + " damage!")
            self.antag.health -= int(dmg[1])
            if self.antag.health <= 0:
                self.antag.health = 0
                break
            print("")
            choice = self.antag.chooseRandomAction()
            dmg = (choice[0], max(0, choice[1] - self.protag.defense))
            if dmg[0]:
                io.say("It did " + Fore.RED + str(int(dmg[1])) + Style.RESET_ALL + " damage!")
            self.protag.health -= int(dmg[1])
            if self.protag.health <= 0:
                self.protag.health = 0
                break
            os.system("clear")
            self.antag.chooseDialogue()
            print("")
            self.antag.enemy_report()
            print("")
            self.protag.report()
        if self.antag.health <= 0:
            print("")
            self.antag.enemy_report()
            io.narr(Fore.GREEN +"You win!")
            self.protag.reward(self.player, exp = self.antag.max_energy, money = round(self.antag.max_health / 5))
            return True
        else:
            print("")
            os.system("clear")
            self.protag.report()
            io.narr(Fore.RED + self.protag.name + " died!")
            self.protaglist.pop(self.protagID)
            if self.protag.name != "You":
                self.setProtag()
                self.start()
            else:
                return False
