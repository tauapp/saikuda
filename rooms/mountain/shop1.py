import util_io as io
from room import Room
from item import Item
import rooms.mountain.penguin3 as penguin3

def scripts(player):
    io.narr("You enter the next room.")
    io.narr("There's a lonely man next to a van. He notices you.")
    io.dialogue("???", "A newcomer, huh?")
    io.dialogue("???", "Nice to see some fresh faces around here.")
    io.dialogue("???", "Come on over. I'm Sollivan, by the way.")
    io.dialogue("Sollivan", "Want to buy some candy?")

def buyCandy(player):
    io.dialogue("Sollivan", "You want some candy, huh?")
    io.dialogue("Sollivan", "Haven't had a good customer in a while. I appreciate it, kiddo.")
    io.dialogue("Sollivan", "Here's the price: 15 Aurum a candy. Take it or leave it.")
    if io.chooseList("What do you do?", ["Buy candy", "Don't buy some"]) == "Buy candy":
        while True:
            io.dialogue("Sollivan", "How many do you want?\n", waitForInput=False)
            print(f"(You have {player.aurum} Aurum.)")
            numtobuy = io.ask("How many candies would you like to buy?")
            if not numtobuy.isdigit():
                print("That's not a number.")
                io.clear()
                continue
            if int(numtobuy) * 15 > player.aurum:
                print("You can't afford that many candies.")
                io.clear()
                continue
            player.aurum -= int(numtobuy) * 15
            for i in range(int(numtobuy)):
                player.items.append(
                    Item(
                        "Hard Candy",
                        10,
                        10
                    )
                )
            if int(numtobuy) == 1:
                io.narr("[You got a Hard Candy.]")
            else:
                io.narr(f"[You got {int(numtobuy)} Hard Candies.]")
            break
    else:
        io.dialogue("Sollivan", "Passing up on the opportunity, huh?")
        io.dialogue("Sollivan", "That's a shame. They're pretty good.")

def talk(player):
    topic = io.chooseList("What do you want to talk about?", 
    ["About Sollivan", "About the mountains", "About his van"])

    if topic == "About Sollivan":
        io.dialogue("Sollivan", "Me, huh?")
        io.dialogue("Sollivan", "Name's Sollivan Tude, but you can call me Solly.")
        io.dialogue("Sollivan", "Used to operate in the Capital, but apparently selling candy in vans is suspicious.")
        io.dialogue("Sollivan", "What a world we live in, huh?")
        io.dialogue("Sollivan", "I haven't seen anyone in ages and I'm freezing all the time, but hey.")
        io.dialogue("Sollivan", "That beats getting the cops called on you every week, right?")
    elif topic == "About the mountains":
        io.dialogue("Sollivan", "Apparently, a lot of people like climbing down this mountain.")
        io.dialogue("Sollivan", "You'd think more people would be going up, but apparently not.")
        io.dialogue("Sollivan", "I only get two or three customers a year.")
        io.dialogue("Sollivan", "That number sucks, but it's better than zero.")
    else:
        io.dialogue("Sollivan", "This van's pretty special to me, you know.")
        io.dialogue("Sollivan", "It took a lot of luck to get to where I am today.")
        io.dialogue("Sollivan", "You know, when I lived down in the Capital, I used to talk to some of the kids on the street.")
        io.dialogue("Sollivan", "And I don't really know why, but their parents gave me money to stop.")
        io.dialogue("Sollivan", "Eventually, I was able to buy this van, and here I am now.")
        io.dialogue("Sollivan", "...")
        io.dialogue("Sollivan", "It's all I have left now.")

def leave(player):
    io.dialogue("Sollivan", "See you around.")
    return penguin3.create(player).start()

actions = [
    ("Buy candy", buyCandy),
    ("Talk", talk),
    ("Leave", leave)
]

def create(player):
    global actions
    map = """
    ____________________
    |                  |
    |           S      |
    |                  |
    |    X             |
    |                  |
    |           V      |
    |__________________|

    X = You
    S = Sollivan
    V = Van
    |_ = Wall
    """

    return Room(map, player,
    scripts = scripts,
    actions = actions)