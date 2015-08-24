from Tools.Scripts.treesync import raw_input
__author__ = 'Joshhy'
from League import *
from View import *
import cmd
import unittest


class Alley(cmd.Cmd):

    league = None

    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Welcome to Pulp Alley, type help for commands")
        self.prompt = "Command: "

    def do_create(self, line):
        """
        This command is used to create a league
        Usage: create 'league name'
        Example: create league2
        """
        if self.league is None:
            self.league = League(line)
            print("Created league: {}".format(line))
        else:
            print("A league called {} currently exists".format(line))

    def do_leader(self, line):
        """
        This command is used to create and add a leader to the active league
        Usage: create 'league name'
        Example: create league2
        """
        params = Validator.get_parameters(line)
        if Validator.check_league(self.league) and Validator.validate_character(params, 11):
            self.league.add_leader(params[0], params[1], params[2], params[3], params[4], params[5], params
            [6], params[7], params[8], params[9], params[10])

    def do_sidekick(self, line):
        params = Validator.get_parameters(line)
        if Validator.check_league(self.league) and Validator.check_for_leader() and Validator.validate_character\
                    (params, 10):
            self.league.add_sidekick(params[0], params[1], params[2], params[3], params[4], params[5], params
            [6], params[7], params[8], params[9])

    def do_ally(self, line):
        params = Validator.get_parameters(line)
        if Validator.check_league(self.league) and Validator.check_for_leader() and Validator.validate_character\
                    (params, 9):
                self.league.add_ally(params[0], params[1], params[2], params[3], params[4], params[5], params
                [6], params[7], params[8])

    def do_follower(self, line):
        params = Validator.get_parameters(line)
        if Validator.check_league(self.league) and Validator.check_for_leader() and Validator.validate_character\
                    (params, 9):
                self.league.add_follower(params[0], params[1], params[2], params[3], params[4], params[5], params
                [6], params[7], params[8])

    def do_display_all(self):
        if self.league.get_leader() is not None:
            View.show_leader(self.league.get_leader())
        if len(self.league.get_allies()) >= 1:
            View.show_chars(self.league.get_allies())
        if len(self.league.get_sidekicks()) >= 1:
            View.show_chars(self.league.get_sidekicks())
        if len(self.league.get_followers()) >= 1:
            View.show_chars(self.league.get_followers())

    def add_league(self, name):
        return League(name)

    def test_league(self):
        league = self.add_league("League1")
        View.print_message(league.add_leader("l1", 1, 2, 3, 4, 5, 6, 7, "animal", "agile", "clever"))
        View.print_message(league.add_ally("a1", 1, 2, 3, 4, 5, 6, 7, "animal"))
        View.print_message(league.add_ally("a2", 1, 2, 3, 4, 5, 6, 7, "animal"))
        View.print_message(league.add_sidekick("s1", 1, 2, 3, 4, 5, 6, 7, "agile", "animal"))
        View.print_message(league.add_sidekick("s2", 1, 2, 3, 4, 5, 6, 7, "agile", "animal"))
        View.print_message(league.add_follower("f1", 1, 2, 3, 4, 5, 6, 7, "agile"))
        View.print_message(league.add_follower("f2", 1, 2, 3, 4, 5, 6, 7, "agile"))


class Validator:

    def check_league(league):
        if league is None:
            print("No league created yet, please create one first")
            return False
        else:
            return True

    def get_parameters(line):
        parameters = line.split(",")
        return parameters

    def validate_character(params, num_params):
        if len(params) is not num_params:
            View.print_message("Invalid amount of parameters, use help to find out correct usage of the command")
            return False
        else:
            return True

    def check_for_leader(league):
        if league.leader is not None:
            return True
        else:
            print("League has no leader yet, please create a leader first")
            return False


def main():
        controller = Alley()
        controller.cmdloop()

if __name__ == '__main__':
    main()

