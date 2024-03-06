#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, satamony):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, satamony):
        """EOF command to exit the program"""
        return True

    def emptyline(self) -> bool:
        pass

    def do_create(self, satamony):
        """Create command to create a new instance"""
        if satamony == "":
            print("** class name missing **")
        else:
            print(satamony)

    def do_show(self, satamony):
        """Show command to show an instance"""
        if satamony == "":
            print("** class name missing **")
        else:
            print(satamony)

    def do_destroy(self, satamony):
        """Destroy command to destroy an instance"""
        if satamony == "":
            print("** class name missing **")
        else:
            print(satamony)

    def do_all(self, satamony):
        """All command to show all instances"""
        if satamony == "":
            print("** class name missing **")
        else:
            print(satamony)

    def default(self, satamony):
        """Default command to handle unknown commands"""
        print(f'{satamony}: command not found')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
