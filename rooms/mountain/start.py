from room import Room
import util_io as io
import rooms.mountain.ravine1 as ravine1

def scripts(player):
    io.narr("Your mission begins now.")
    io.narr("You awaken.")
    io.narr("You stand up and shake off the snow on your clothes.")

def lookAround(player):
    io.narr("You look around. You're by a cliff.")
    io.narr("Going down the cliff seems to be the only way to go.")
    io.narr("You trudge closer and closer to the edge.")
    fallorfloat = io.chooseList("Would you like to fall or fly?", ["Fall", "Fly"])
    if fallorfloat == "Fall":
        io.narr("You take a deep breath and take a leap.")
    else:
        io.narr("You take a leap of faith and flap your arms.")
    io.narr("You wake up on the snow. Seems like it broke your fall.")
    io.narr("You stand up, relieved.")
    return ravine1.create(player).start()

def create(player):
    map = ""
    actions = [
        ("Look around", lookAround)
    ]
    return Room(map, player, 
    enemychance=0, 
    exits = {},
    scripts = scripts,
    actions=actions)