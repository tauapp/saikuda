import util_io as io
from room import Room

exits = {}

def scripts(player):
    io.narr("With the penguin gone, you approach the door.")
    io.narr("The door's unlocked and you open it.")
    io.narr("You step inside and the door shuts behind you, leaving you trapped in the room.")
    io.narr("In the dim light of the room, you can see a water cooler and an exit door.")
    io.narr("The exit door seems to have some kind of electric lock on it.")
    io.narr("There is a sign next to the door. It reads:")
    io.dialogue("Sign", "The only way to beat electricity (Press [Enter to continue])")
    io.dialogue("Sign", "Is to call upon its worst enemy.")

def lookAtLock(player):
    global exits
    io.narr("You observe the electric lock. It has no keyhole.")
    options = ["Break the lock", "Nothing"]
    if player.state["holdingwater"] == True:
        options.append("Pour water on lock")
    whattodo = io.chooseList("What do you do?", )
    if whattodo == "Break the lock":
        io.narr("You try to break the lock, but it's too strong.")
    elif whattodo == "Pour water on lock":
        io.narr("You pour water on the lock.")
        io.narr("You see sparks coming out of the lock. It's been short-circuited!")
        player.state["holdingwater"] = False
        #TODO: Next room
        exits["South"] = None
        io.narr("You hear a click. The door opens!")

    else:
        io.narr("You decide to leave the lock alone.")

def lookAtWaterCooler(player):
    io.narr("The water cooler is full. There is a stack of foam cups next to it.")
    takeaglass = io.chooseList("Do you take a glass?", ["Yes", "No"])
    if takeaglass == "Yes":
        io.narr("You take a glass and fill it with refreshing water.")
        player.state["holdingwater"] = True
    else:
        io.narr("You decide you're not thirsty.")

def drinkWater(player):
    if player.state["holdingwater"] == True:
        player.state["holdingwater"] = False
        io.narr("You drink the water, quenching your thirst.")

def create(player):
    global exits
    map = """
    ________________
    |              |
    |       O      |
    | X           L|
    |              |
    |______________|

    X = You
    O = Water Cooler
    L = Locked Door
    |_ = Wall
    """

    actions = [
        ("Look at lock", lookAtLock),
        ("Look at water cooler", lookAtWaterCooler)
    ]

    return Room(map, player, 
    enemychance=0, 
    exits = exits,
    scripts=scripts,
    actions=actions)