from copy import deepcopy
import os
from attack import Attack
from battle import Battle
from fightable import Fightable
from room import Room
import util_io as io
import rooms.mountain.puzzle1 as puzzle1

def scripts(player):

    #Saved player object for respawns
    save = deepcopy(player)

    io.narr("You walk into a ravine. It's narrow and cold.")
    look = io.chooseList("What do you do?", ["Rush forward", "Look ahead"])
    if look == ""

    penguin = Fightable(
        "Pinko",
        max_health=50,
        max_energy = 25,
        defense = 0,
        attack = 5,
        attack_list=[
            Attack(
                name="Wing Attack",
                intensity=3,
                cost=15,
                req=0,
                speed=0.05
            )
        ],
        level=0,
        exp=0,
        leveltable=[]
    )
    penguin.friendship = (0,3)
    penguin.conversations = [
        "You complement Pinko on its sleek feathers. It wholeheartedly agrees.",
        "You asked Pinko why it's fighting. You don't understand a word of what it said.",
        "You asked Pinko what it likes to do in its free time. You don't understand a word of what it said.",
    ]
    penguin.dialogues = [
        "Pinko stands proudly.",
        "Pinko looks at you with a blank stare.",
        "Pinko prepares its next attack.",
    ]

    penguin.art = """
        __
     -=(o '.
        '.-.\\
        /|  \\\\
        '|  ||
         _\_):,_
    """

    if not Battle(player, penguin).start():
        io.narr("Respawning...")
        io.clear()
        return create(save).start()
    

def create(player):
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
    exits = {},
    scripts=scripts)