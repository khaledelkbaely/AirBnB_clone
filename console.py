#!/usr/bin/python3
"""module for cmd main function"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

current_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.

    It sub-classes Python's `cmd.Cmd` class which provides a simple framework
    for writing line-oriented command interpreters.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """
        handle empty line input
        """
        pass

    def do_EOF(self, line):
        """EOF to quit the program"""
        print()
        return True

    def do_quit(self, line):
        """quit to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Quit when signals EOF (C-d)")

    def do_create(self, line):
        """create new instance
        """
        argv = line.strip().split()
        if len(argv) == 0:
            print('** class name missing **')
            return
        if argv[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        obj = current_classes[argv[0]]()
        print(obj.id)

    def do_show(self, line):
        """print string representation of instance
        """
        argv = line.strip().split()

        if not self.validate_input(argv):
            return

        key = '{}.{}'.format(argv[0], argv[1])
        if not storage.exist(key):
            print('** no instance found **')
            return

        obj = storage.all()[key]
        if obj:
            print(obj)

    def do_destroy(self, line):
        """delete instance
        """
        argv = line.strip().split()

        if not self.validate_input(argv):
            return

        key = '{}.{}'.format(argv[0], argv[1])
        if not storage.exist(key):
            print('** no instance found **')
            return
        obj = storage.all()[key]
        if obj:
            storage.destroy(key)

    def do_all(self, line):
        """show all instances
        """
        argv = line.strip().split()
        if argv and argv[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        objs = storage.all()
        print([str(o) for o in objs.values()])

    def do_update(self, line):
        """update instance
        """
        argv = line.strip().split(maxsplit=3)

        if not self.validate_input(argv):
            return
        key = '{}.{}'.format(argv[0], argv[1])
        if not storage.exist(key):
            print('** no instance found **')
            return
        if len(argv) == 2:
            print('** attribute name missing **')
            return
        if len(argv) == 3:
            print('** value missing **')
            return
        storage.update(*argv[0:4])

    def validate_input(self, argv):
        """helper function"""
        if len(argv) == 0:
            print('** class name missing **')
            return False
        if argv[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(argv) == 1:
            print('** instance id missing **')
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
