import pickle

def saveToFile(room):
    pickle.dump(room, open("saves/save.pickle", "wb"))