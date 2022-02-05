from room import Room
import util_io as io

def actions():
    io.narr("It’s freezing. It’s cold. No point in crying about it. You need to get downhill.")
    io.narr("Or is it downmountain...?")
    io.narr("You stand up but slip on ice. You are on the edge of a cliff.")
    fallOrFloat = io.chooseList("Would you like to fall or float?", ["Fall", "Float"])
    if fallOrFloat == "Fall":
        io.narr("You fall down the cliff. Thankfully, there’s fluffy snow where you fall, and you are not hurt.")
    else:
        io.narr("You channel your inner strength and try to float above the abyss...")
        io.narr("You fall. Gravity exists whether you like it or not.")

def create(player):
    map = ""
    return Room(map, player, 
    enemychance=0, 
    description="You are on the top of a cold mountain.", 
    exits = {"South": None},
    actions = actions)