__author__ = 'Joshhy'
from Character import *


class Sidekick(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability1, ability2):
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.char_type = 'Sidekick'
        self.level = 3
        self.slot = 3
        self.abilities = []
        self.add_ability(ability1)
        self.add_ability(ability2)

