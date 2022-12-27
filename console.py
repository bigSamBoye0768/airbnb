#!/usr/bin/python3

from models import storage
import shlex

import cmd
from termcolor import colored
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    intro = colored('''Welcome to the airbnb shell.
Type 'help;' or '?' for help. \n''', 'yellow')
    prompt = colored("(airbnb)> ", "cyan")
    __classes = {
        'BaseModel',
        'User',
        'State',
        'City',
        'Place',
        'Amenity',
        'Review'
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass




    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <classname>
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """

        if len(arg) == 0:
            print(colored("** class name missing **", "red"))
        elif arg not in HBNBCommand.__classes:
            print(colored("** class doesn't exist **", "red")) 
        else:
            cls_dict = {'BaseModel':BaseModel, 'User':User, 'Place':Place, 'State':State, 'Amenity':Amenity, 'Review':Review, 'City':City}
            instance = cls_dict[arg]()
            print(colored(instance.id, 'green'))
            instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""

        args = arg.split(' ')

        if not arg:
            print(colored("** class name missing **", "red"))
        elif args[0] not in HBNBCommand.__classes:
            print(colored("** class doesn't exist **", "red"))
        elif len(args) == 1:
            print(colored("** instance id missing **", "red"))
        else:
            # query all object as a dictionary
            all_obj = storage.all()
            for k, v in all_obj.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if args[0] == obj_name and args[1] == obj_id:
                    print(v)
                    return
            print(colored("** no instance found **", "red"))
            

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id (save the change into the JSON file)."""

        args = arg.split(' ')

        if not arg:
            print(colored("** class name missing **", "red"))
        elif args[0] not in HBNBCommand.__classes:
            print(colored("** class doesn't exist **", "red"))
        elif len(args) == 1:
            print(colored("** instance id missing **", "red"))
        else:
            # query all object as a dictionary
            all_obj = storage.all()
            for k, v in all_obj.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if args[0] == obj_name and args[1] == obj_id:
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
                else:
                    print(colored("** no instance found **", "red"))
                    return


    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        all_obj = storage.all()
        if len(arg) > 0 and arg not in HBNBCommand.__classes:
            print(colored("** class doesn't exist **", "red"))
        else:
            obj_list = []
            for obj in all_obj.values():
                if len(arg) > 0 and arg == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(sel, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        args = arg.split(" ")
        all_obj = storage.all()

        if not arg:
            print(colored("** class name missing **", "red"))
            return
        elif args[0] not in HBNBCommand.__classes:
            print(colored("** class doesn't exist **", "red"))
            return
        else:
            for k, v in all_obj.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if args[0] == obj_name and args[1] == obj_id:
                    if len(args) == 2:
                        print(colored("** attribute name missing **", "red"))
                    elif len(args) == 3:
                        print(colored("** value missing **", "red")) 
                    else:
                        setattr(v, args[2], args[3])
                        storage.save()
                    return
                        
            print(colored("** no instance found **", "red"))

                    







        

# instance = BaseModel()
# print(instance.id)




if __name__ == '__main__':
    HBNBCommand().cmdloop()