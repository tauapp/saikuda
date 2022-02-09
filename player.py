class Player:

    #Money
    aurum = 0

    #Temporary state for rooms
    state = dict()

    def __init__(self, name, creatures, items):
        self.creatures = creatures
        self.items = items
        self.name = name
        for c in creatures:
            c.items = self.items