import util_io as io
import room as Room

exits = dict()
roomstate = dict()

def scripts(player):
    io.narr("Phew. That was close.")
    io.narr("It seems like you're in another puzzle room.")
    io.narr("There's a small kitchen with a fridge, cabinet, and stove.")

def lookAtCabinet(player):
    global roomstate
    if roomstate.get("cabinetHasPot"):
        io.narr("You open the cabinet. There's a pot inside.")
        takepot = io.chooseList("Take it?", ["Yes", "No"])
        if takepot == "Yes":
            player.state["holdingpot"] = 1
            roomstate["cabinetHasPot"] = False
            io.narr("You take the pot.")
        else:
            io.narr("You leave the cabinet alone.")
    else:
        io.narr("The cabinet's empty.")

def lookAtDoor(player):
    io.narr("This door also appears to have an electric lock.")
    #The holdingpot state returns 1 if player is holding a pot with air or ice, 2 if the pot has water.
    choices = ["Break the lock", "Nothing"]
    if player.state.get("holdingpot") == 2:
        choices.insert(1, "Pour water on lock")
    whattodo = io.chooseList("What do you do?", choices)
    if whattodo == "Break the lock":
        io.narr("You try to break the lock.")
        io.narr("It isn't budging. It seems like you're not strong enough.")
    elif whattodo == "Pour water on lock":
        io.narr("You pour water on the lock.")
        player.state["holdingpot"] = 1
        io.narr("You see sparks coming out of the lock. It's been short-circuited!")
    else:
        io.narr("You leave the door alone.")

def lookAtSign(player):
    io.dialogue("Sign", "Didn't you learn anything from the last puzzle?")

def lookAtStove(player):
    pass

actions = [
    ("Look at sign", lookAtSign),
    ("Look at door", lookAtDoor),
    ("Look at cabinet", lookAtCabinet),
    ("Look at stove", lookAtStove)
]

def create(player):
    global exits
    global actions
    global roomstate
    roomstate["cabinetHasPot"] = True
    map = """
    ____________________
    |                  |
    |         F C S    |
    |                  |
    |    X            L|
    |                  |
    |                  |
    |__________________|

    X = You
    |_ = Wall
    L = Locked door
    F = Fridge
    C = Cabinet
    S = Stove
    """

    return Room(map, player,
    enemychance = 0,
    exits = exits,
    scripts = scripts,
    actions = actions
    )