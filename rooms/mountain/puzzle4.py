from room import Room
import util_io as io
import rooms.mountain.shop1 as shop1

exits = dict()
roomState = {
    "timesSearchedLeaves": 0
}

def scripts(player):
    io.narr("You're in what seems to be another puzzle room.")
    io.narr("There's a stove, a sign, and a random pile of leaves.")

def readSign(player):
    io.dialogue("Sign", "You can find the wood inside what grows from the wood.")
    io.dialogue("Sign", "Use the wood to destroy the wood.")

def lookAtDoor(player):
    global exits
    io.narr("It's a plain wooden door with a good-old deadbolt lock.")
    io.narr("No messing around with electricity this time.")
    opts = ["Break the lock", "Leave it alone"]
    #holdingStick returns 1 if player is holding a stick, 2 if the stick is on fire.
    if player.state.get("holdingStick") == 2:
        opts.insert(0, "Burn down door")
    choice = io.chooseList("What do you do?", opts)
    if choice == "Break the lock":
        io.narr("You try to break the lock.")
        io.narr("It isn't budging. It seems like you're not strong enough.")
    elif choice == "Burn down door":
        io.narr("You use your flaming stick to burn down the door.")
        io.narr("You can now move on the the next room!")
        exits["Next room"] = shop1.create(player)
    else:
        io.narr("You leave the door alone.")

def lookAtStove(player):
    global roomState
    io.narr("You look at the stove. It doesn't interest you in the slightest.")
    opts = []
    if not roomState.get("stoveOn"):
        opts.append("Turn on stove")
    if roomState.get("stoveOn"):
        opts.append("Turn off stove")
    if player.state.get("holdingStick") == 1 and roomState.get("stoveOn"):
        opts.append("Light stick on fire")
    opts.append("Leave the stove alone")
    
    choice = io.chooseList("What do you do?", opts)
    if choice == "Turn on stove":
        io.narr("You turned on the stove.")
        player.state["stoveslefton"] += 1
        roomState["stoveOn"] = True
    elif choice == "Turn off stove":
        io.narr("You turned off the stove.")
        player.state["stoveslefton"] -= 1
        roomState["stoveOn"] = False
    elif choice == "Light stick on fire":
        io.narr("You jab the end of the stick into the flames.")
        io.narr("You are effectively holding a flaming torch.")
        player.state["holdingStick"] = 2
    else:
        io.narr("You leave the stove alone.")

def lookAtLeaves(player):
    global roomState
    io.narr("It's a random pile of leaves.")
    whattodo = io.chooseList("What do you do?", ["Search pile", "Nothing"])
    if whattodo == "Search pile":
        roomState["timesSearchedLeaves"] += 1
        if roomState["timesSearchedLeaves"] == 3:
            io.narr("What's this? There's a dry stick in the leaves.")
            io.narr("You pick it up.")
            player.state["holdingStick"] = 1
        else:
            io.narr("You couldn't find anything in the pile.")


actions = [
    ("Look at sign", readSign),
    ("Look at door", lookAtDoor),
    ("Look at stove", lookAtStove),
    ("Look at leaves", lookAtLeaves)
]

def create(player):
    global actions
    global exits
    map = """
    ____________________
    |            S     |
    |                  |
    |                  |
    |    X             |
    |                  |
    |          L       |
    |__________________|

    X = You
    S = Stove
    L = Pile of leaves
    |_ = Wall
    """

    return Room(map, player,
    enemychance=0.75,
    scripts = scripts,
    exits = exits,
    actions=actions
    )