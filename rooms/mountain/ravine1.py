from copy import deepcopy
import os
from attack import Attack
from battle import Battle
from fightable import Fightable
from room import Room
import util_io as io
import rooms.mountain.puzzle1 as puzzle1
import enemies.mountain.pinko as pinko

exits = dict()

def scripts(player):
    global exits

    #Saved player object for respawns
    save = deepcopy(player)

    io.narr("You walk into a ravine. It's narrow and cold.")
    look = io.chooseList("What do you do?", ["Rush forward", "Look ahead"])
    if look == "Rush forward":
        io.narr("You make a run for it.")
        io.narr("You quickly stop, noticing something in the way. It's a... penguin?")
    else:
        io.narr("You look ahead. there seems to be a door in the distance.")
        io.narr("You notice a shadowy figure rapidly approaching.")

    penguin = pinko.create()

    if not Battle(player, penguin).start():
        io.narr("Respawning...")
        io.clear()
        return create(save).start()
    if look == "Rush forward":
        io.narr("It seems like there's a large door at the end of the ravine.")
    else:
        io.narr("You finally reached the large door.")
    nextroom = puzzle1.create(player)

    openit = io.chooseList("Open the door?", ["Yes", "No"])
    exits["Through the door"] = nextroom
    if openit == "Yes":
        io.narr("You step inside.")
        return nextroom.start()
    else:
        io.narr("You stand in front of the door and do absolutely nothing.")
        return

def create(player):
    global exits
    map = """
    __________________
    |
    | X
    |_________________

    X = You
    |_ = Wall
    """
    return Room(map, player, 
    enemychance=0, 
    exits = exits,
    scripts=scripts)