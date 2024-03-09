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
    prompt = '(hbnb)'

    def do_quit(self, satamony):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, satamony):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, satamony):
        """Create command to create a new instance"""
        args = parse_argument(satamony)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, satamony):
        """Show command to show an instance"""
        args = parse_argument(satamony)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, satamony):
        """Destroy command to destroy an instance"""
        args = parse_argument(satamony)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, satamony):
        """All command to show all instances"""
        args = parse_argument(satamony)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instances = [
                str(value) for key, value in models.storage.all().items()
                if len(args) == 0 or key.split(".")[0] == args[0]
            ]
            print(instances)

    def do_update(self, satamony):
        """Update command to update an instance"""
        args = parse_argument(satamony)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                instance = models.storage.all()[key]
                setattr(instance, args[2], args[3])
                instance.save()
            
    
    def default(self, satamony):
        print(parse_argument(satamony))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
