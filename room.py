from battle import Battle
import util_io as io

class Room:

    exits = {
        "North": None,
        "South": None,
        "East": None,
        "West": None,
    }

    def __init__(self, map, player, enemy = None, description = "", exits = {}):
        self.map = map
        self.enemy = enemy
        self.description = description

    def start(self):
        if self.description != None:
            io.narr(self.description)
        if self.enemy != None:
            io.narr("A wild " + self.enemy.name + " appears!")
            #Start battle between player and enemy
            if Battle(self.player, self.enemy).start() == False:
                #TODO: Go back to previous room
                pass
        self.move()

    def move(self):
        room = self.exits[io.chooseList("Where do you want to go?", self.exits.keys)]
        return room.start()

