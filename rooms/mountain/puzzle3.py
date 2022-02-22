import util_io as io
import room as Room

exits = dict()

def scripts(player):
    io.narr("Phew. That was close.")
    io.narr("It seems like you're in another puzzle room.")
    io.narr("There's a small kitchen with a fridge, cabinet, and stove.")

def lookAtCabinet(player):
    pass

def lookAtDoor(player):
    pass

def lookAtSign(player):
    pass

def lookAtStove(player):
    pass

actions = [
    
]

def create(player):
    global exits
    global actions
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