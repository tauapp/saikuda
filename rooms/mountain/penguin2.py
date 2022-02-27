from room import Room
import util_io as io
from _blessed import Terminal
import rooms.mountain.puzzle4 as puzzle4

def scripts(player):
    term = Terminal()
    io.narr("You walk into the next room.")
    io.narr("Oh no.")
    io.narr("It seems like you've walked right into the Emperor's flippers.")
    io.dialogue("Emperor Pinko", "There you are!")
    io.dialogue("Emperor Pinko", "You may have escaped last time, but this time will be different!")
    io.dialogue("Emperor Pinko", "How arrogant. You must think that you're better than the Emperor himself!")
    whattosay = io.chooseList("What do you do?", ["Tell him he's pathetic", "Stay silent"])
    if whattosay == "Tell him he's pathetic":
        io.dialogue("Emperor Pinko", "How dare you. You think you have any right to say that?")
        io.dialogue("Emperor Pinko", f"You ran away like a coward, and you have the gall to call { term.bold('me') } pathetic?")
    else:
        io.dialogue("Emperor Pinko", "No words left to say? You can't even own up to it?")
        io.dialogue("Emperor Pinko", "That condescending glare... You say nothing, but I know your intentions!")
    io.dialogue("Emperor Pinko", "Tch. It's time to prove my worth.")
    io.dialogue("Emperor Pinko", "Perish!")

    io.narr("Emperor Pinko charges!")

    io.narr("CLANK!")
    io.narr("In the blink of an eye, the Emperor has been knocked out.")
    io.narr(f"Who saved you? Was it the { term.bold('mystery person') }?")
    io.narr("You don't know.")

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
        scripts = scripts,
        exits = {
            "Next Room": puzzle4.create(player)
        }
    )