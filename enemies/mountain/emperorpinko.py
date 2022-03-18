from attack import Attack
from fightable import Fightable
import ai_engines.three_ahead as engine


def create():
    emperor = Fightable(
            "Emperor Pinko",
            max_health=250,
            max_energy=100,
            defense=0,
            attack=2,
            attack_list=[
                Attack(
                    "Peck",
                    2,
                    4,
                    0.03
                ),
                Attack(
                    "Wing Attack",
                    5,
                    40,
                    0.05
                ),
                Attack(
                    "Ice Storm",
                    13,
                    100,
                    0.04
                )
            ],
            level=0,
            exp=0,
            leveltable=[
                #TODO: Finish this
            ]
    )

    emperor.ai_engine = engine.lookThreeAhead

    emperor.friendship = (0, 10)
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

    emperor.reward = (100, 100)

    return emperor