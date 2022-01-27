class Fightable:

    name = ""

    health = 100

    max_health = 100

    defense = 0

    attack = 5

    attack_list = []

    energy = 100

    max_energy = 100

    def __init__(self, name, max_health, max_energy, defense, attack, attack_list):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.defense = defense
        self.attack = attack
        self.attack_list = attack_list
        self.energy = max_energy
        self.max_energy = max_energy