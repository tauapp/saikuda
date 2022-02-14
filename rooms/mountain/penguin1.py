import util_io as io
from room import Room

def scripts(player):
    io.narr("You enter a new room.")
    io.narr("It's still dark. It would have been nice if you had a flashlight, but you don't.")
    io.narr("You hear footsteps. Who is it this time?")
    io.narr("Shadowy figures surround you.")
    io.narr("The figures are small, and you faintly recognize their shape.")
    io.narr("A larger figure makes its way to the forefront.")
    io.dialogue("???", "So you've finally arrived.")
    io.dialogue("???", "We didn't expect another one of you, but you just had to show your face, didn't you?")
    io.dialogue("???", "Unfortunately for you, this is where is all ends.")
    io.dialogue("???", "Don't act confused. We know why you're here.")
    io.dialogue("???", "Fun fact about us: We don't take kindly to people like you.")
    io.dialogue("???", "Any last words before you kick the bucket?")
    whatdoto = io.chooseList("What do you do?", ["Stand menacingly", "Say you don't want to fight"])
    if whatdoto == "Stand menacingly":
        io.dialogue("???", "Don't try to be too tough. You're outnumbered and we will easily finish you.")
    else:
        io.dialogue("???", "You don't want to fight, Well, maybe I should just let you free...")
        io.dialogue("???", "Just kidding! You think you can get away that easily?")
        io.dialogue("???", "I'll anser that for you. You're not getting away. You're going to die.")
    io.dialogue("???", "Alright, enough blabbering. My soldiers, rage! My soldiers, fight!")
    io.narr("You hear squawks from the crowd, and you realize that they're penguins.")
    io.narr("Someone turns on the lights and you realize how outnumbered you are.")
    io.dialogue("???", "My name's Emperor Penguin. Better remember that, because it's the last name you'll ever hear!")
    io.narr("Emperor Penguin charges!")
    io.narr("You're frozen in fear. He gets closer... and closer...")
    io.narr("...And then proceeds to trip on a pebble.")
    io.dialogue("Emperor Penguin", "Ow! My flippers!")
    io.narr("There are squawks of laughter from the crowd.")
    io.dialogue("Emperor Penguin", "Hey! Stop laughing! I'm your captain!")
    io.narr("You take this opportunity to escape.")
    io.narr("You run back into the previous room and hide behind a corner.")
    io.dialogue("Emperor Penguin", "Where did they go? Soldiers, find them!")
    io.narr("A horde of penguins emerge from the room to search for you.")
    io.narr("They can't find you. Now's your chance.")
    escapetactic = io.chooseList("What do you do?", ["Sprint past Emperor Penguin", "Tiptoe past him like a coward"])
    if escapetactic == "Tiptoe past him like a coward":
        player.state["isCool"] = False
        io.narr("You delicately tiptoe past Emperor Penguin without making a sound.")
        io.narr("What a coward.")
        io.narr("You make it safely to the next room.")
    else:
        player.state["isCool"] = True
        io.narr("You run past Emperor Penguin like the cool person you are.")
        io.dialogue("Emperor Penguin", "HEY! YOU CAN'T JUST-")
        io.narr("You use his face as a bouncepad, silencing him.")
        io.narr("Being the awesome person you are, you pull off a flip in mid-air.")
        io.narr("Big mistake. Instead of landing gracefully, you land on your face.")
        io.narr("Ouch. That hurt.")
        io.narr("You quickly shut the door behind you. Mission successful.")
        io.narr("You gained 15 street cred.")

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
        scripts = scripts,
        exits = {
            "South": None
        }
    )