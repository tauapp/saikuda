from room import Room

def create(player):
    map = """
    | X |
    |   |
    |____
    X= You, |_ = Wall
    """
    return Room(map, player, enemychance=0, description="You are on the top of a cold mountain.", exits = {"North": None})