from attack import Attack
from fightable import Fightable
import util_io as io

def create():
    pinko = Fightable(
            "Pinko",
            max_health=50,
            max_energy = 25,
            defense = 0,
            attack = 1,
            attack_list=[
                Attack(
                    name="Wing Attack",
                    intensity=5,
                    cost=15
                )
            ],
            level=0,
            exp=0,
            leveltable=[]
        )
    pinko.friendship = (0,3)
    pinko.conversations = [
            "You complement Pinko on its sleek feathers. It wholeheartedly agrees.",
            "You asked Pinko why it's fighting. You don't understand a word of what it said.",
            "You asked Pinko what it likes to do in its free time. You don't understand a word of what it said.",
        ]
    pinko.dialogues = [
            "Pinko stands proudly.",
            "Pinko looks at you with a blank stare.",
            "Pinko prepares its next attack.",
        ]

    pinko.art = """
            __
        -=(o '.
            '.-.\\
            /|  \\\\
            '|  ||
            _\_):,_
        """
    
    return pinko