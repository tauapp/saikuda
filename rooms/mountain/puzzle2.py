import util_io as io
from room import Room
from player import Player
from weapon import Weapon
import rooms.mountain.penguin1 as penguin1

exits = dict()

def scripts(player: Player):
    io.narr("You walk through the door... and you're in another room. Here we go again.")
    io.narr("You look ahead, and you notice a lurking shadow.")
    io.narr("This one is different. It seems... human.")

def approachHale(player):
    global actions
    io.narr("You approach the figure.")
    io.chooseList("What do you say?", ["Who are you?", "Hello...?"])
    io.narr("The figure retreats, alarmed by your appearance.")
    io.narr("They left a wrench on the ground.")
    pickupwrench = io.chooseList("Pick it up?", ["Yes", "No"])
    if pickupwrench == "Yes":
        io.narr("You pick up the wrench, grasping it firmly.")
        player.creatures[0].equipWeapon(Weapon("Wrench", 1.5))
    else:
        io.narr("You decide to leave the wrench behind.")

    print("")
    io.narr("You prepare yourself for the next puzzle. You hear a creak.")
    io.narr("The door is open! Looks like you can skip this puzzle.")
    actions.remove(("Approach the figure", approachHale))
    exits["Next room"] = penguin1.create(player)

actions = [
    ("Approach the figure", approachHale)
]


def create(player):
    global exits
    global actions
    map = """
    ____________________
    |                  |
    |                  |
    |                  |
    |    X             |
    |                  |
    |                  |
    |__________________|

    X = You
    |_ = Wall
    """

    return Room(
        map = map,
        player = player,
        scripts = scripts,
        enemychance = 0,
        exits = exits,
        actions=actions
    )