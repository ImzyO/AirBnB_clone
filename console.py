#!/usr/bin/python3
"""
a program called console.py that contains
the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb)"
    Classes = ["BaseModel"]

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

    def empty_line(self):
        """empty line shouldn't execute anything"""
        pass

    def create_new_instance(self, classname):
        if len(classname) == 0:
            print("** class name missing **")
        elif classname not in self.Classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel.classname
            new_instance.save
            print(new_instance.id)

if __name__ == '__main__':
        HBNBCommand().cmdloop()
