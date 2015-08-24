from Abilities import Abilities

__author__ = 'Josh'


class Character(object):

    def __init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning, abilities, char_type=None, slot=None, level=None):
        self.name = name
        self.health = health
        self.brawl = brawl
        self.shoot = shoot
        self.dodge = dodge
        self.might = might
        self.finesse = finesse
        self.cunning = cunning
        self.char_type = char_type
        self.level = level
        self.slot = slot
        self.abilities = abilities

    def get_char_name(self):
        return self.name

    def get_char_info(self):
        return "%s  |   %s   |   %s   |   %s   |   %s   |   %s   |   %s   " \
               "|   %s   |   %s"%\
               (self.char_type, self.name, self.health, self.brawl, self.shoot, self.dodge, self.might, self.finesse,
                self.cunning)

    def add_ability(self, abilityName):
        # Author of this module is Jessie Velano
        if abilityName == "agile" or abilityName == "Agile":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Dodge is increased by +1"
                                                                       " die.", abilityLevel=1))
            return True
        elif abilityName == "animal" or abilityName == "Animal":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character may not shoot, but adds +1d"
                                                                       " to two other skills.", abilityLevel=1))
            return True
        elif abilityName == "clever" or abilityName == "Clever":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Cunning is increased by +1"
                                                                       " die", abilityLevel=1))
            return True
        elif abilityName == "fierce" or abilityName == "Fierce":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Brawl is increased by +1"
                                                                       " die.", abilityLevel=1))
            return True
        elif abilityName == "marksman" or abilityName == "Marksman":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Shoot is increased by +1"
                                                                       " die.", abilityLevel=1))
            return True
        elif abilityName == "mighty" or abilityName == "Mighty":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Might is increased by +1"
                                                                       " die.", abilityLevel=1))
            return True
        elif abilityName == "savvy" or abilityName == "Savvy":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character's Finesse is increased by +1"
                                                                       " die.", abilityLevel=1))
            return True
        elif abilityName == "speedy" or abilityName == "Speedy":
            self.abilities.append(Abilities(abilityName, abilityEffect="This character may run up to 15\""
                                                                       " - instead of 12\".", abilityLevel=1))
            return True
        elif abilityName == "athletic" or abilityName == "Athletic":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, shift this character's "
                                                                           "dice-type up when rolling for Might or "
                                                                           "Finesse.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "brute" or abilityName == "Brute":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character may re-roll"
                                                                           " one Brawl or Might die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "crafty" or abilityName == "Crafty":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character may re-roll "
                                                                           "one Dodge or Cunning die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "daredevil" or abilityName == "Daredevil":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character receives a"
                                                                           " +1d bonus when rolling for a "
                                                                           "Peril.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "eagleeyed" or abilityName == "EagleEyed" or abilityName == "Eagle-eyed":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character's close range is 12\", and"
                                                                           " their long range is 48\"-instead of 6\""
                                                                           " and24\".", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "finagler" or abilityName == "Finagler":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, shift this character's "
                                                                           "dice-type up when rolling for Finesse or "
                                                                           "Cunning.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "intrepid" or abilityName == "Intrepid":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character may move in any direction"
                                                                           " when they successfully dodge an attack "
                                                                           "or peril.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "sharp" or abilityName == "Sharp":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character may re-roll"
                                                                           " one Shoot or Finesse"
                                                                           " die.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "specialist" or abilityName == "Specialist":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, shift this character's"
                                                                           " dice-type up when rolling for Cunning or "
                                                                           "Might.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "stealthy" or abilityName == "Stealthy":
            if self.level >= 2:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character may hide as an action"
                                                                           " - instead of a full"
                                                                           " action.", abilityLevel=2))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "astute" or abilityName == "Astute":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character's Shoot and Finesse"
                                                                           " dice-type are not lowered due to "
                                                                           "injuries.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "brash" or abilityName == "Brash":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character is not limited to rushing"
                                                                           " the closest enemy.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "deadeye" or abilityName == "Deadeye":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character is not limited to shooting"
                                                                           " the closest enemy.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "deductive" or abilityName == "Deductive":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="As an action for this character, you may"
                                                                           " draw one Fortune card.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "hardened-veteran" or abilityName == "Hardened-Veteran":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character ignores the multiple combats"
                                                                           " penalty.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "indomitable" or abilityName =="Indomitable":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character may re-roll one Recovery"
                                                                           " check per turn.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "muscle-of-steel" or abilityName == "Muscle-Of-Steel":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character's Brawl and Might dice-type"
                                                                           " are not lowered due to "
                                                                           "injuries.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "shrewd" or abilityName =="Shrewd":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="This character's Dodge and Cunning "
                                                                           "dice-type are not lowered due to "
                                                                           "injuries.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "quick-shot" or abilityName =="Quick-Shot":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character may shift"
                                                                           " their shooting dice-type down to gain a"
                                                                           " +2d bonus only against targets in close "
                                                                           "range.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "quick-strike" or abilityName == "Quick-Strike":
            if self.level >= 3:
                self.abilities.append(Abilities(abilityName, abilityEffect="Once per turn, this character may shift"
                                                                           " their brawling dice-type down to gain a"
                                                                           " +2d bonus.", abilityLevel=3))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        elif abilityName == "lucky-devil" or abilityName == "Lucky-Devil":
            if self.level >= 4:
                self.abilities.append(Abilities(abilityName, abilityEffect="When this leader activates, the opponent "
                                                                           "may not play any Fortune "
                                                                           "cards.", abilityLevel=4))
                return True
            else:
                print("***Character Level Is Too Low!***")
                return False
        else:
            print("***Ability Does Not Exist!***")
            return False

    def display_ability(self):
        #Author of this module is Jessie Velano
        splitterChars = "------------------------------------------------------------------------------"
        for i in self.abilities:
            print(splitterChars)
            print(Abilities.__str__(i))

        print(splitterChars)

