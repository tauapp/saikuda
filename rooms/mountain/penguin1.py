import util_io as io
from room import Room
import rooms.mountain.puzzle3 as puzzle3

def scripts(player):
    io.narr("You enter a new room.")
    io.narr("It's still dark. It would have been nice if you had a flashlight, but you don't.")
    io.narr("You hear footsteps. Shadowy masses surround you.")
    io.narr("A larger figure makes its way to the forefront.")
    io.dialogue("???", "So you've finally arrived.")
    io.dialogue("???", "We didn't expect another one of you, but you just had to show your face around here, didn't you?")
    io.dialogue("???", "Unfortunately for you, this is where is all ends.")
    io.dialogue("???", "Don't act confused. We know why you're here.")
    io.dialogue("???", "Fun fact about us: We don't take kindly to people like you.")
    io.dialogue("???", "Any last words before you kick the bucket?")
    whatdoto = io.chooseList("What do you do?", ["Stand menacingly", "Say you don't want to fight"])
    if whatdoto == "Stand menacingly":
        io.dialogue("???", "You think you're tough? Nobody's scared of a weakling like you.")
    else:
        io.dialogue("???", "You don't want to fight, Well, maybe I should just let you free...")
        io.dialogue("???", "Just kidding! You think you can get away that easily?")
        io.dialogue("???", "I'll answer that for you. You're not getting away. You're going to die.")
    io.dialogue("???", "Alright, enough blabbering. My soldiers, rage! My soldiers, fight!")
    io.dialogue("???", "My name's Emperor Pinko. Better remember that, because it's the last name you'll ever hear!")
    io.narr("Emperor Pinko charges!")
    io.narr("He gets closer... and closer...")
    io.narr("...And then proceeds to trip on a pebble.")
    io.dialogue("Emperor Pinko", "Ow! My flippers!")
    io.narr("There are squawks of laughter from the crowd.")
    io.dialogue("Emperor Pinko", "Stop laughing at me, you incompetent fools!")
    io.narr("You take this opportunity to escape.")
    io.narr("You hide behind a corner in the last room.")
    io.dialogue("Emperor Pinko", "Where did they go? Soldiers, find them!")
    io.narr("A horde of penguins emerges from the room to search for you.")
    io.narr("They can't find you. Now's your chance.")
    escapetactic = io.chooseList("What do you do?", ["Sprint past Emperor Pinko", "Tiptoe past him like a coward"])
    if escapetactic == "Tiptoe past him like a coward":
        player.state["isCool"] = False
        io.narr("You delicately tiptoe past Emperor Penguin without making a sound.")
        io.narr("What a coward.")
        io.narr("You make it safely to the next room.")
    else:
        player.state["isCool"] = True
        io.narr("You make a run for it, jumping off Emperor Pinko's face.")
        io.narr("You do a flip in the air, attempting to land gracefully...")
        io.narr("Only to land on your face. Ouch. That hurt.")
        io.narr("You're now in the next room.")
    return puzzle3.create(player).start()

def create(player):
    map = """
    ____________________
    |                  |
    |                  |
    |                  |
    |    X      ?      |
    |                  |
    |                  |
    |__________________|

    X = You
    ? = Mysterious Figure
    |_ = Wall
    """

    return Room(
        map = map,
        player = player,
        scripts = scripts
    )