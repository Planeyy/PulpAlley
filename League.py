__author__ = 'Joshhy'
from Leader import *
from Ally import *
from Sidekick import *
from Follower import *


class League:
    def __init__(self, league_name):
        self.league_name = league_name
        self.allies = []
        self.sidekicks = []
        self.followers = []
        self.leader = None

    def get_leader(self):
        return self.leader

    def get_followers(self):
        return self.followers

    def get_allies(self):
        return self.allies

    def get_sidekicks(self):
        return self.sidekicks

    def add_leader(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability1, ability2, ability3):
        leader = Leader(name, health, brawl, shoot, dodge, might, finesse, cunning, ability1, ability2, ability3)
        if self.leader is None:
            self.leader = leader
            print("Successfully added leader with the name: %s" % name)
        else:
            print("A leader with the name %s already exists in the league called: %s" % (self.leader.get_char_name(),
                                                                                          self.league_name))

    def add_ally(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability):
        ally = Ally(name, health, brawl, shoot, dodge, might, finesse, cunning, ability)
        if not self.check_for_duplicate_char(self.allies, ally.get_char_name()):
            self.allies.append(ally)
            print("Successfully added ally %s to league %s" % (ally.get_char_name(), self.league_name))
        else:
            print("Ally %s already exists in league %s" % (ally.get_char_name(), self.league_name))

    def add_sidekick(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability1, ability2):
        sidekick = Sidekick(name, health, brawl, shoot, dodge, might, finesse, cunning, ability1, ability2)
        if not self.check_for_duplicate_char(self.sidekicks, sidekick.get_char_name()):
            self.sidekicks.append(sidekick)
            print("Successfully added sidekick %s to league %s" % (sidekick.get_char_name(), self.league_name))
        else:
            print("Sidekick %s already exists in league %s" % (sidekick.get_char_name(), self.league_name))

    def add_follower(self, name, health, brawl, shoot, dodge, might, finesse, cunning, ability):
        follower = Follower(name, health, brawl, shoot, dodge, might, finesse, cunning, ability)
        if not self.check_for_duplicate_char(self.followers, follower.get_char_name()):
            self.followers.append(follower)
            print("Successfully added follower %s to league %s" % (follower.get_char_name(), self.league_name))
        else:
            print("Follower %s already exists in league %s" % (follower.get_char_name(), self.league_name))

    def check_for_duplicate_char(self, char_list, name):
        is_duplicate = False
        for char in char_list:
            if char.get_char_name() is name:
                is_duplicate = True
        return is_duplicate
