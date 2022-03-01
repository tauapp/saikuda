import util_io as io
from room import Room
from item import Item

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
            io.dialogue("Sollivan", "How many do you want?", waitForInput=False)
            print(f"(You have {player.aurum} Aurum.")
            numtobuy = io.ask("How many candies would you like to buy?")
            if not numtobuy.isdigit():
                print("That's not a number.")
                continue
            if int(numtobuy) * 15 > player.aurum:
                print("You can't afford that many candies.")
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
                io.narr(f"[You got {int(numtobuy)} Hard Candies.")
    else:
        io.dialogue("Sollivan", "Passing up on the opportunity, huh?")
        io.dialogue("Sollivan", "That's a shame. They're pretty good.")

def talk(player):
    pass

def leave(player):
    pass

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