from room import Room
import util_io as io

def scripts(player):
    io.narr("You walk into the next room.")
    io.narr("Oh no.")
    io.narr("It seems like you've walked right into the Emperor's flippers.")
    io.dialogue("Emperor Pinko", "There you are!")
    io.dialogue("Emperor Pinko", "You may have escaped last time, but this time will be different!")
    io.dialogue("Emperor Pinko", "How arrogant. You must think that you're better than the Emperor himself!")

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
        scripts = scripts
    )