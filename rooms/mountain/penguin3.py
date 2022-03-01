import io as util_io
from room import Room

def scripts(player):
    io.narr("You're in the next room.")
    io.narr("Guess who it is this time.")
    io.dialogue("Emperor Pinko", "YOU.")
    io.dialogue("Emperor Pinko", "After all this time, I've finally cornered you.")
    io.dialogue("Emperor Pinko", "I thought this would be quick, but you wouldn't allow that.")
    io.dialogue("Emperor Pinko", "You've embarressed me not just one, but twice.")
    io.dialogue("Emperor Pinko", "I will beat you this time, and you will pay dearly.")
    if io.chooseList("What do you do?", [
        "Tell him he'll never beat you",
        "Tell him to knock it off"]) == "Tell him he'll never beat you":
        io.dialogue("Emperor Pinko", "Wrong. Here and now, I will beat you.")
        io.dialogue("Emperor Pinko", "It's not just about my Pinko pride anymore.")
        io.dialogue("Emperor Pinko", "It's about humbling the arrogant human who thinks they can defy me!")
    else:
        io.dialogue("Emperor Pinko", "Knock it off? KNOCK IT OFF?")
        io.dialogue("Emperor Pinko", "You humiliate me twice, and you tell me to knock it off?")
        io.dialogue("Emperor Pinko", "THATS IT! You're finished.")
    io.dialogue("Emperor Pinko", "Say goodbye.")
    

def create(player):
    map = """
    ____________________
    |                  |
    |                  |
    |                  |
    |    X      P      |
    |                  |
    |                  |
    |__________________|

    X = You
    P = Emperor Pinko
    |_ = Wall
    """

    return Room(map, player, 
    scripts = scripts)