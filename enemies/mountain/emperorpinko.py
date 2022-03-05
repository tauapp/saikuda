from attack import Attack
from fightable import Fightable


def create():
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
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
        "TODO",
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
    return emperor