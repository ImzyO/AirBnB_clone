#!/usr/bin/python3
"""
a program called console.py that contains
the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb)"

    def do_quit(self, quit):
        """exiting/quiting the program"""
        return True

    def help_on_quit(self):
        """help on quit"""
        print("Quit command to exit the program")

    def do_EOF(self, EOF):
        """End of program efore executing"""
        return True

    def help_on_EOF(self):
        """help on EOF"""
        print("End of File command: end of program reached")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
