import util_io as io
from room import Room
from fightable import Fightable
from attack import Attack
from copy import deepcopy
from battle import Battle

def scripts(player):
    save = deepcopy(player)

    io.narr("You're in the next room.")
    io.narr("Guess who it is this time.")
    io.dialogue("Emperor Pinko", "YOU.")
    io.dialogue("Emperor Pinko", "After all this time, I've finally cornered you.")
    io.dialogue("Emperor Pinko", "I thought this would be quick, but you wouldn't allow that.")
    io.dialogue("Emperor Pinko", "You've embarressed me not just one, but twice.")
    io.dialogue("Emperor Pinko", "I will beat you this time, and you will pay dearly.")
    if io.chooseList("What do you do?", [
        "Tell him he'll never beat you",
        "Tell him to knock it off"]) == "Tell him he'll never beat you":
        io.dialogue("Emperor Pinko", "Wrong. Here and now, I will beat you.")
        io.dialogue("Emperor Pinko", "It's not just about my Pinko pride anymore.")
        io.dialogue("Emperor Pinko", "It's about humbling the arrogant human who thinks they can defy me!")
    else:
        io.dialogue("Emperor Pinko", "Knock it off? KNOCK IT OFF?")
        io.dialogue("Emperor Pinko", "You humiliate me twice, and you tell me to knock it off?")
        io.dialogue("Emperor Pinko", "THATS IT! You're finished.")
    io.dialogue("Emperor Pinko", "Say goodbye.")

    emperor = Fightable(
        "Emperor Pinko",
        max_health=1000,
        max_energy=1000,
        defense=50,
        attack=10,
        attack_list=[
            Attack(
                "Peck",
                2,
                50,
                0.03
            ),
            Attack(
                "Wing Attack",
                6,
                100,
                0.05
            ),
            Attack(
                "Ice Storm",
                30,
                950,
                0.04
            )
        ],
        level=0,
        exp=0,
        leveltable=[
            #TODO: Finish this
        ]
    )

    emperor.friendship = (0, 15)
    emperor.conversations = [
        "You tell Emperor Pinko that he doesn't need to fight.",
        "You tell Emperor Pinko that you are innocent.",
        "You ask Emperor Pinko about why he's fighting you.",
        "You tell Emperor Pinko that you did nothing wrong."
    ]

    emperor.dialogues = [
        #TODO
        "Among us sussy",
        "Like the hit game among us",
        "Ing dong lingus",
        "Tetris is amingus",
        "Fling flag fringo",
        "Indigo",
        "Rick rick ricko",
        "Lim li la lo zee zo"
    ]

    emperor.randomizeDialogue = False

    emperor.art = """
        __
     -=(o '.
        '.-.\\
        /|  \\\\
        '|  ||
         _\_):,_
    """

    if not Battle(player, emperor).start():
        io.narr("Respawning...")
        io.clear()
        return create(save).start()

def create(player):
    map = """
    ____________________
    |                  |
    |                  |
    |                  |
    |    X      P      |
    |                  |
    |                  |
    |__________________|

    X = You
    P = Emperor Pinko
    |_ = Wall
    """

    return Room(map, player, 
    scripts = scripts)