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

    def help_empty_line(self):
        """command to help with empty line"""
        print("command helpswith emptyline")

    def create_new(self, classname):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if len(classname) == 0:
            print("** class name missing **")
        elif classname not in self.Classes:
            print("** class doesn't exist **")
        else:
            new_instance = ("{} {}".format(classname))
            new_instance.save
            print(new_instance.id)

    def help_new(self):
        """help new"""
        print("command to help with new instance creation")

    def do_show(self, *args):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
        elif len(args[1]) == 0:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def help_show(self):
        """command to help show"""
        print("command to help show using show")

     def do_destory(self, *args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        # comments for do_destroy and do_show methods
        # if classname missing; prints
        # if class name doesn't exist prints
        # if id missing;prints instanceid missing
        # if instance of classname doesn't exist for id;
        # print no instance found

        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
        elif len(args[1]) == 0:
            print("** instance id missing **")
        else:
            print("** no instance found **")

     destroyed = destroy("{} {}".format(arg[0], arg[1])           
     destroyed.save
     print(destroyed)

     def help_destroy(self):
        """command to help destroy"""
        print("command to help destroy")    

     def do_all(self, *args):
        """
        Prints all string representation of all instances based or 
        not on the class name. Ex: $ all BaseModel or $ all
        """
        if args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
        print(str("[{}]".format(args)))

    def help_all(self):
        """helps with all arguments inputed"""
        print("Command to show all instances")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
