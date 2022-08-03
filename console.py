#!/usr/bin/python3
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """command processor class."""
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """EOF command to exit the program.
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_create(self, args):
        """Creates a new instance.
        """
        strg = shlex.split(args)
        if len(strg) == 0:
            print("** class name missing **")
            return False
        else:
            cls_name = strg[0]
            if cls_name not in classes.keys():
                print("class doesn't exist")
            else:
                obj = self.classes[cls_name]()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        strg = shlex.split(args)

        if len(strg) == 0:
            print("** class name missing **")
            return False

        if len(strg) > 0:
            if strg[0] not in classes.keys():
                print("** class doesn't exist **")
                return False

        if len(strg) > 1:
            if strg[1] == "":
                print("** instance id missing **")
                return False

        key = f"{strg[0]}.{strg[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return False

        obj = storage.all()[key]
        print(f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id.
        """
        strg = shlex.split(args)
        obj_id = shlex.split(args)[1]

        if len(strg) == 0:
            print("** class name missing **")
            return False

        if len(strg) > 0:
            if strg[0] not in classes.keys():
                print("** class doesn't exist **")
                return False

        if len(strg) > 1:
            if strg[1] == "":
                print("** instance id missing **")
                return False

        key = f"{strg[0]}.{strg[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return False
        storage.all().pop(key)
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        strg = shlex.split(args)
        if len(strg) > 0:
            cls_name = strg[0]
            if cls_name in classes.keys():
                ar = []
                class_name = classes[cls_name]
                for key in storage.all().keys():
                    if cls_name in key.split("."):
                        obj = storage.all()[key]
                        ar.append(f"[{class_name}] ({obj.id}) {obj.__dict__}")
                print(ar)
            else:
                print("** class doesn't exist **")
        else:
            ar = []
            for key in storage.all().keys():
                cls_name = key.split(".")[0]
                class_name = classes[cls_name]
                obj = storage.all()[key]
                ar.append(f"[{class_name}] ({obj.id}) {obj.__dict__}")
            print(ar)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        strg = shlex.split(args)

        if len(strg) == 0:
            print("** class name missing **")
            return False

        if len(strg) > 0:
            if strg[0] not in classes.keys():
                print("** class doesn't exist **")
                return False

        if len(strg) > 1:
            if strg[1] == "":
                print("** instance id missing **")
                return False

            key = f"{strg[0]}.{strg[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
                return False

        if len(strg) > 2:
            if strg[2] == "":
                print("** attribute name missing **")
                return False

            if strg[2] in ["id", "created_at", "updated_at"]:
                return False

        if len(strg) > 3:
            if strg[3] == "":
                print("** value missing **")
                return False

        key = f"{strg[0]}.{strg[1]}"
        atrr_name = strg[2]
        atrr_value = strg[3]

        obj = storage.all()[key]
        z = atrr_value.split(".")
        if atrr_value.isdigit():
            setattr(obj, atrr_name, int(atrr_value))

        if len(z) == 2 and z[0].isdigit() and z[1].isdigit():
            setattr(obj, atrr_name, float(atrr_value))

        setattr(obj, atrr_name, atrr_value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
