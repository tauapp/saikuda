import util_io as io
from room import Room
import rooms.mountain.puzzle2 as puzzle2

exits = {}



def scripts(player):
    io.narr("The door shuts behind you.")
    io.narr("There's a water cooler, a sign, and a locked door.")
    io.narr("This seems like a puzzle room.")

def lookAtLock(player):
    global exits
    io.narr("You observe the door. It appears to have an electric lock.")
    options = ["Break the lock", "Nothing"]
    if player.state.get("holdingwater") == True:
        options.insert(1, "Pour water on lock")
    whattodo = io.chooseList("What do you do?", options)
    if whattodo == "Break the lock":
        io.narr("You try to break the lock.")
        io.narr("It isn't budging. It seems like you're not strong enough.")
    elif whattodo == "Pour water on lock":
        actions.remove(("Drink water", drinkWater))
        io.narr("You pour water on the lock.")
        #If lock already shorted, do nothing
        if exits.get("South"):
            io.narr("The lock has already short circuited.")
            return
        io.narr("You see sparks coming out of the lock. It's been short-circuited!")
        player.state["holdingwater"] = False
        exits["Next room"] = puzzle2.create(player)
        io.narr("You hear a click. The door opens!")
        io.narr("You can now exit this room.")

    else:
        io.narr("You decide to leave the lock alone.")

def lookAtWaterCooler(player):
    global actions
    io.narr("The water cooler has a stack of foam cups next to it.")
    takeaglass = io.chooseList("Do you take a glass?", ["Yes", "No"])
    if takeaglass == "Yes":
        io.narr("You take a glass and fill it with refreshing water.")
        player.state["holdingwater"] = True
        actions.append(("Drink water", drinkWater))

    else:
        io.narr("You decide you're not thirsty.")

def drinkWater(player):
    if player.state.get("holdingwater") == True:
        player.state["holdingwater"] = False
        io.narr("You drink the water, quenching your thirst.")
        player.creatures[0].health = player.creatures[0].max_health
        player.creatures[0].energy = player.creatures[0].max_energy
        io.narr("Your Health and Energy was restored.")
        actions.remove(("Drink water", drinkWater))

def lookAtSign(player):
    io.dialogue("Sign", "The only way to beat electricity")
    io.dialogue("Sign", "Is to call upon its worst enemy.")

actions = [
    ("Read sign", lookAtSign),
    ("Look at door", lookAtLock),
    ("Look at water cooler", lookAtWaterCooler),
]

def create(player):
    global exits
    global actions
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
    

    return Room(map, player, 
    enemychance=0, 
    exits = exits,
    scripts=scripts,
    actions=actions)