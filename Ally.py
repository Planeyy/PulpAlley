__author__ = 'Joshhy'
from Character import *


class Ally(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability):
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.char_type = 'Ally'
        self.level = 2
        self.slot = 2
        self.abilities = []
        self.add_ability(ability)

