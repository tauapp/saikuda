import util_io as io
from room import Room
from player import Player
from weapon import Weapon

def scripts(player: Player):
    io.narr("You walk through the door… and you’re in another room. Here we go again.")
    io.narr("It’s dark, and it’s cold.")
    io.narr("The noise of clanking and metal fills the room, and a shadowy figure seems to be moving around.")
    io.narr("Though you may be a bit apprehensive, you approach the figure.")
    io.chooseList("What do you say?", ["Who are you?", "Hello...?"])
    io.narr("The shadowy figure seems to retreat, alarmed by your appearance.")
    io.narr("You can’t quite see where they go. Who was that?")
    io.narr("You notice they left a wrench on the ground.")
    pickUpWrench = io.chooseList("Pick it up?", ["Yes", "No"])
    if pickUpWrench == "Yes":
        io.narr("You pick up the wrench, grasping it firmly.")
        player.creatures[0].equipWeapon(
            Weapon("Wrench", 1.5)
        )
    else:
        io.narr("Against your better judgement, you leave the wrench behind.")

    io.narr("You prepare yourself for the next puzzle.")
    io.narr("You hear a creak... looking at the exit door, you see that it's barely open!")
    io.narr("Looks like you can skip this puzzle.")


def create(player):
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
        exits = {
            "South": None
        }
    )