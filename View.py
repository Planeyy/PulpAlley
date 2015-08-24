__author__ = 'Joshhy'
from Character import *

class View:
    header = "Char type | Name | Health | Brawl | Shoot | Dodge | Might | Finesse | Cunning"
    splitterChars = "------------------------------------------------------------------------------"
    def print_message(msg):
        print(msg)

    def show_chars(char_list):
        for char in char_list:
            print(View.header)
            print(View.splitterChars)
            print(char.get_char_info())
            char.display_ability()
            print()

    def show_leader(leader):
        print(View.header)
        print(View.splitterChars)
        print(leader.get_char_info())
        leader.display_ability()
        print()

