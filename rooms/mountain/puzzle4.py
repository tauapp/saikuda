from room import Room
import util_io as io


exits = dict()
roomState = dict()

def scripts(player):
    io.narr("You're in what seems to be another puzzle room.")
    io.narr("There's a stove, a sign, and a random pile of leaves.")

def readSign(player):
    io.dialogue("Sign", "Good luck solving this puzzle, because I know you can't.")
    io.dialogue("Sign", "What do you mean I'm not being helpful?")
    io.dialogue("Sign", "Do you know the things I go through every day...")
    io.narr("The sign goes on and on about why it doesn't want to help.")
    io.narr("You get bored and decide to stop reading it.")

def lookAtDoor(player):
    global exits
    io.narr("It's a plain wooden door with a good-old deadbolt lock.")
    io.narr("No messing around with electricity this time.")
    opts = ["Break the lock", "Leave it alone"]
    #holdingStick returns 1 if player is holding a stick, 2 if the stick is on fire.
    if roomState.get("holdingStick") == 2:
        opts.prepend("Burn down door")
    choice = io.chooseList("What do you do?", opts)
    if choice == "Break the lock":
        io.narr("You try to break the lock.")
        io.narr("It isn't budging. It seems like you're not strong enough.")
    elif choice == "Burn down door":
        io.narr("You use your flaming stick to burn down the door.")
        io.narr("You can now move on the the next room!")
        exits["Next room"] = None
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
    if roomState.get("holdingStick") == 1 and roomState.get("stoveOn"):
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
        io.narr("Don't burn your hands off. You didn't pay your health insurance premiums last month.")
        roomState["holdingStick"] = 2
    else:
        io.narr("You leave the stove alone.")
        


actions = [
    ("Look at sign", readSign),
    ("Look at door", lookAtDoor),
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
    scripts = scripts,
    exits = exits,
    actions=actions
    )