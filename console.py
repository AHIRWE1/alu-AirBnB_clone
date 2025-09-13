#!/usr/bin/python3
"""
Console for AirBnB clone.
Handles the command interpreter for creating, updating,
showing, and deleting objects.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objs.values() if type(obj).__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = self.parse_update_args(arg)
        if args is None:
            return
        class_name, obj_id, attr_name, attr_value = args
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        # Don't update id, created_at, updated_at
        if attr_name in ["id", "created_at", "updated_at"]:
            return
        # Cast value to correct type if possible
        try:
            attr_type = type(getattr(obj, attr_name, str(attr_value)))
            if attr_type is int:
                attr_value = int(attr_value)
            elif attr_type is float:
                attr_value = float(attr_value)
        except Exception:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def parse_update_args(self, arg):
        """Helper to parse update arguments and handle errors"""
        args = []
        in_quotes = False
        current = ""
        for c in arg:
            if c == '"':
                in_quotes = not in_quotes
            elif c == " " and not in_quotes:
                if current:
                    args.append(current)
                    current = ""
            else:
                current += c
        if current:
            args.append(current)
        if len(args) == 0:
            print("** class name missing **")
            return None
        if args[0] not in classes:
            print("** class doesn't exist **")
            return None
        if len(args) == 1:
            print("** instance id missing **")
            return None
        if len(args) == 2:
            print("** attribute name missing **")
            return None
        if len(args) == 3:
            print("** value missing **")
            return None
        return args[:4]


if __name__ == "__main__":
    HBNBCommand().cmdloop()