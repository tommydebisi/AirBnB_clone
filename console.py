#!/usr/bin/python3
"""
An Interpreter for my Airbnb clone
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import shlex
import re
import sys


class HBNBCommand(cmd.Cmd):
    """
    A class that inherits from the cmd module
    """

    prompt = "(hbnb) "
    all_models = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    def precmd(self, line: str) -> str:
        """
            Runs after every input in console
            Args:
                line: the inputted text
        """
        regex = [
                 r"^(\w+)\.(\w+)\((.*)\)",
                 r'(\w+)\.(\w+)\("([\w\d-]+)",\s({[\d\w\s\':\",]*})\)'
                ]
        if re.search(regex[1], line):
            reg_pat = re.findall(regex[1], line)
            args = self.update_dict(reg_pat)
            return args
        elif re.search(regex[0], line):
            reg_pat = re.findall(regex[0], line)
            c_name, method = reg_pat[0][0], reg_pat[0][1]
            args = reg_pat[0][2]

            if args:
                temp = [arg.strip("'") for arg in reg_pat[0][2].split(", ")]
                args = " ".join(temp)

            return "{} {} {}".format(method, c_name, args)
        else:
            return super().precmd(line)

    def do_EOF(self, args):
        """
        Handles the EOF command
        """

        print()
        return True

    def do_quit(self, args):
        """
        Handles the quit command
        """

        return True

    def help_quit(self):
        """
        help for the quit command
        """

        print("Quit command to exit the program")

    def do_create(self, args):
        """
        Create new instances
        """

        if args:
            parsed = shlex.split(args)
            if parsed[0] in self.all_models:
                new_obj = eval(parsed[0])()
                print(new_obj.id)
                new_obj.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        msg = ["create a new instance of an object",
               "Usage: create <class name>"]
        print("\n".join(msg))

    def do_show(self, args):
        """
        Shows the string rep. of an instance based on the class name and id
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")

        else:
            if args[0] in self.all_models:
                print("** instance id missing **")
                return
            else:
                print("** class doesn't exist **")
                return
            if len(args > 1):
                all_objs = storage.all()
                key = ".".join(args[:2])
                if key in all_objs:
                    obj = all_objs[key]
                    print(obj)
                else:
                    print("** no instance found **")

    def help_show(self):
        """
        help for the "show" command
        """

        msg = ["Prints the string rep. of an ins based on class name & id",
               "Usage: show <class name> <id>"]
        print("\n".join(msg))

    def do_count(self, args):
        """
        Counts an object passed or all if none is passed
        """

        all_objs = storage.all()
        all_objs_list = list()
        if args:
            args = shlex.split(args)
            if args[0] in self.all_models:
                for key in all_objs:
                    if type(all_objs[key]).__name__ == args[0]:
                        all_objs_list.append(str(all_objs[key]))
            else:
                print("** class doesn't exist **")
                return
        else:
            for key in all_objs:
                all_objs_list.append(str(all_objs[key]))
        print(len(all_objs_list))

    def do_destroy(self, args):
        """
        Deletes an instance based onthe class name
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")

        else:
            if args[0] in self.all_models:
                print("** instance id missing **")
                return
            else:
                print("** class doesn't exist **")
                return
            if len(args) > 1:
                all_objs = storage.all()
                key = ".".join(args[:2])
                if key in all_objs:
                    del all_objs[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def help_destroy(self):
        """
        help for the "destroy" command
        """

        msg = ["Deletes an instance based on the class name",
               "Usage: destroy <class name> <id>"]
        print("\n".join(msg))

    def do_all(self, args):
        """
        string representation of all instances on the class(optional) provided
        """

        all_objs = storage.all()
        all_objs_list = list()
        if args:
            args = shlex.split(args)
            if args[0] in self.all_models:
                for key in all_objs:
                    if type(all_objs[key]).__name__ == args[0]:
                        all_objs_list.append(str(all_objs[key]))
            else:
                print("** class doesn't exist **")
                return
        else:
            for key in all_objs:
                all_objs_list.append(str(all_objs[key]))
        print(all_objs_list)

    def help_all(self):
        """
        help function for "all" command
        """

        msg = ["string rep. of all ins on the class(optional) provided",
               "Usage: all [<class name>]"]
        print("\n".join(msg))

    def emptyline(self):
        """
        does nothing when no command is passed
        """

        pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) >= 1:
            if args[0] not in self.all_models:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return

        if len(args) >= 2:
            all_objs = storage.all()
            key = ".".join(args[0:2])
            if key in all_objs:
                obj = all_objs[key]
            else:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return

        if len(args) == 3:
            print("** value missing **")
            return

        if len(args) > 4 and args[4] == "1":
            del args[4]
            args = args[2:]
            for i in range(0, len(args), 2):
                setattr(obj, args[i], args[i + 1])
                obj.save()
        else:
            setattr(obj, args[2], args[3])
            obj.save()

    def help_update(self):
        """
        Help for "update" command
        """

        msg = ["updates obect with new attributes",
               "Usage: update <class name> <id> <attribute <value>"]
        print("\n".join(msg))

    def update_dict(self, reg_pat):
        """
        A parser for updating dict
        """

        c_name, method, ins_id = reg_pat[0][0], reg_pat[0][1], reg_pat[0][2]
        dict_args = reg_pat[0][3]
        if dict_args:
            dict_args = eval(dict_args)
            flag = 1
            args = ""
            for key, val in dict_args.items():
                attr_val_pair = "\"{}\" \"{}\" ".format(key, val)
                args += attr_val_pair
                if flag:
                    args += "1 "
                    flag = 0

        return "{} {} {} {}".format(method, c_name, ins_id, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
