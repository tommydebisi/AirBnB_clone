#!/usr/bin/python3
"""
    Interative CLI console
"""
import cmd
from models.base_model import BaseModel
import json as js
import shlex # treat the args same as C shell
from models import storage

def id_checker(class_name, id):
    """
        checker the classname and id
        if present in file

        Args:
            class_name: name of class
            id: unique number

        Returns:
            True if the id present with class
            false if not
    """
    with open('file.json', encoding='utf-8') as filename:
        check_dict = js.load(filename)

    if check_dict.get(class_name + "." + id):
        return True
    return False

class HBNBCommand(cmd.Cmd):
    """
        Command class
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
            overrrides the default command when emptyline is entered
        """
        pass

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
            help for quit
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, args):
        """
            Alternate Command to exit program
        """
        print()
        return True

    def do_create(self, args):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if args:
            args = BaseModel()
            args.save()
            print(args.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """
            Prints the string representation of an instance
            based on the class name and id

            Args:
                args: arguments inputted
        """
        parsed = shlex.split(args) # split string to list
        if not args:
            print("** class name missing **")
        elif parsed[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(parsed) == 1:
            print("** instance id missing **")
        else:
            try:
                with open('file.json', encoding='utf-8') as filename:
                    dict_checker = js.load(filename)

                if obj := dict_checker.get(parsed[0] + '.' + parsed[1]):
                    print(BaseModel(**obj))
                else:
                    print("** no instance found **")
            except Exception:
                pass

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id

            Args:
                args: arguments inputted
        """
        parsed = shlex.split(args) # split string to list
        if not args:
            print("** class name missing **")
        elif parsed[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(parsed) == 1:
            print("** instance id missing **")
        else:
            try:
                full_key = parsed[0] + '.' + parsed[1]
                with open('file.json', encoding='utf-8') as filename:
                    dict_checker = js.load(filename)

                if dict_checker.get(full_key):
                    del dict_checker[full_key]
                    print(dict_checker)

                    with open('file.json', 'w', encoding='utf-8') as filename:
                        js.dump(dict_checker, filename)
                else:
                    print("** no instance found **")
            except Exception:
                pass

    def do_all(self, args):
        """
            Prints all string representation of all instances
            based or not on the class name
        """

        parsed = shlex.split(args)
        if args and parsed[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            try:
                with open('file.json', encoding='utf-8') as filename:
                    dict_checker = js.load(filename)

                obj_list = list()
                for val in dict_checker.values():
                    obj_list.append(str(BaseModel(**val)))

                print(obj_list)
            except Exception:
                pass

    def do_update(self, args):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute
        """

        parsed_args = shlex.split(args)
        if not args:
            print("** class name missing **")
        elif parsed_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(parsed_args) == 1:
            print("** instance id missing **")
        elif not id_checker(parsed_args[0], parsed_args[1]):
            print("** no instance found **")
        elif len(parsed_args) == 2:
            print("** attribute name missing **")
        elif len(parsed_args) == 3:
            print("** value missing **")
        else:
            try:
                print("Parsing: {}".format(str(parsed_args[3])))
                full_name = parsed_args[0] + "." + parsed_args[1]
                with open('file.json', encoding='utf-8') as filename:
                    get_dict = js.load(filename)

                get_dict[full_name].update({parsed_args[2] : parsed_args[3]})

                with open('file.json', 'w', encoding='utf-8') as filename:
                    js.dump(get_dict,filename)
            except Exception:
                pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
