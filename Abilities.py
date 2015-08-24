__author__ = 'Jessie'


class Abilities(object):

    def __init__(self, abilityName, abilityEffect=None, abilityLevel=None):
        self.abilityName = abilityName
        self.abilityEffect = abilityEffect
        self.abilityLevel = abilityLevel

    def __str__(self):
        return "Ability: {} - {}".format(self.abilityName, self.abilityEffect)