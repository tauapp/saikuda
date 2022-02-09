from room import Room
import util_io as io
import rooms.mountain.ravine1 as ravine1

def scripts(player):
    io.narr("Your mission begins now.")
    io.narr("...")
    io.narr("You awaken.")
    io.narr("The snow blows against you, and you can feel your teeth chattering.")
    io.narr("Your heart is pounding. You’re completely and utterly alone.")
    io.narr("You stare out into the distance, looking for some sign of civilization.")
    io.narr("But you see nothing.")
    io.narr("Desperate, you look around for some sort of escape.")
    io.narr("You quickly notice you are at the edge of a cliff.")
    io.narr("You look around further, trying to see if there's another way.")
    io.narr("But there's none. The cliff is your only escape.")
    fallOrFloat = io.chooseList("Would you like to fall or fly?", ["Fall", "Fly"])
    if fallOrFloat == "Fall":
        io.narr("You approach the cliff, though cautious.")
        io.narr("You know you're going to regret this, and yet... it has to happen.")
        io.narr("You take a deep breath to calm yourself, and fighting against your fear, you jump off the cliff.")
    else:
        io.narr("You reach into your heart, searching for the strength you need.")
        io.narr("You jump into the air, attempting to fly.")
        io.narr("You frantically flap your arms as if they were wings." )
        io.narr("But you fall regardless, plummeting down into the abyss.")

    io.narr("...")
    io.narr("You wake up once again, on the ground blanketed by comforting snow.")
    io.narr("That could've been worse.")

def create(player):
    map = ""
    return Room(map, player, 
    enemychance=0, 
    exits = {"South": ravine1.create(player)},
    scripts = scripts)