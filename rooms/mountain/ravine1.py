from attack import Attack
from battle import Battle
from fightable import Fightable
from room import Room
import util_io as io

def actions(player):
    io.narr("You walk into a ravine. The walls are narrow, and there’s only one direction you can go.")
    io.narr("At the end of the ravine, you can barely make out a large door.")
    io.narr("Wait... what's that shadowy shape in your way?")
    io.narr("You look closer...")
    io.narr("It's a penguin... holding a comically large hammer?")
    io.narr("It charges!")

    penguin = Fightable(
        "Penguin",
        max_health=50,
        max_energy = 25,
        defense = 0,
        attack = 5,
        attack_list=[
            Attack(
                name="Hammer Smash",
                intensity=3,
                cost=15,
                req=0
            )
        ],
        level=0,
        exp=0,
        leveltable=[]
    )
    penguin.friendship = (0,3)
    penguin.conversations = [
        "You complement Penguin on its sleek feathers. It wholeheartedly agrees.",
        "You asked Penguin where it got its hammer. You don't understand a word of what it said.",
        "You asked Penguin if it likes to play video games. It mumbles something about a broken window.",
    ]
    penguin.dialogues = [
        "Penguin stands proudly, and then falls over.",
        "Penguin looks at you with a blank stare.",
        "Penguin mumbles something about a broken window.",
    ]

    Battle(player, penguin).start()
    

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
    exits = {"South": None},
    actions=actions)