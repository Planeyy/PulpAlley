__author__ = 'Joshhy'
from Character import *


class Follower(Character):
    def __init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability):
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.char_type = 'Follower'
        self.level = 1
        self.slot = 1
        self.abilities = []
        self.add_ability(ability)

