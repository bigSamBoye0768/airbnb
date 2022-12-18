#!/usr/bin/python3

import cmd
from termcolor import colored

class HBNBCommand(cmd.Cmd):
    intro = colored('''Welcome to the airbnb shell.
Type 'help;' or '\h' for help. \n''', 'yellow')
    prompt = colored("(airbnb)> ", "cyan")

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self):
        return True








if __name__ == '__main__':
    HBNBCommand().cmdloop()