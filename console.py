#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from helper import parse_argument
import models

classes = {
        "BaseModel": BaseModel,
        "State": State,
        "Review": Review,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "User": User
    }


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the class name"""
        args = arg.split()
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items()
               if not args or v.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or updating attribute
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = parse_argument(arg)
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized"""
        args = arg.split(".")
        if len(args) < 2:
            print("*** Unknown syntax:", arg)
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "count()":
            print(len([v for k, v in models.storage.all().items()
                       if v.__class__.__name__ == args[0]]))
        elif args[1].startswith("show("):
            self.do_show(args[0] + " " + args[1][6:-2])
        elif args[1].startswith("destroy("):
            self.do_destroy(args[0] + " " + args[1][9:-2])
        elif args[1].startswith("update("):
            self.do_update(args[0] + " " + args[1][7:-1])
        else:
            print("*** Unknown syntax:", arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
