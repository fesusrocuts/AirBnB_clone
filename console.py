#!/usr/bin/env python3
"""Class Console"""

import cmd
from datetime import datetime, date, time
from models.base_model import BaseModel, storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB Console"""

    airbnb_models = {"BaseModel": BaseModel, "User": User}
    prompt = "(hbnb) "

    def do_quit(self, command):
        """Quit command line"""
        return True

    def do_EOF(self, command):
        """Quit command line"""
        return True

    def emptyline(self):
        """Repeat prompt"""
        pass

    def do_create(self, command):
        """This method create new objet type BaseMo"""

        command_split = command.split()
        name_object = command_split[0]
        if len(command) == 0 or command is None:
            print("** class name missing **")
        elif command not in self.airbnb_models:
            print("** class doesn't exist **")
        else:
            print(User())
            #print(new_instance.id)
            #new_instance.save()

    def do_show(self, command):
        """Prints the string representation of an instance"""
        split_command = command.split()
        if len(split_command) == 0:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            all_dict_json = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            try:
                print("[{}] ({}) {}".format(split_command[0], split_command[1],
                                            all_dict_json[key_dict]))
            except:
                print("** no instance found **")

    def do_destroy(self, command):
        """Deletes an instance based on the class name and id"""
        split_command = command.split()
        if len(split_command) == 0:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            all_dict_json = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            try:
                all_dict_json.pop(key_dict)
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, command=""):
        """Prints all string representation of all instances"""
        instances = storage.all()
        if not command:
            print(instances)
        else:
            if command not in self.airbnb_models:
                print("** class doesn't exist **")
                return
            else:
                allItemsModel = []
                for key, value in instances.items():
                    if command in key:
                        allItemsModel.append(BaseModel(**value).__str__())
                print(allItemsModel)

    def do_update(self, command):
        """Updates an instance based on the class name and id"""
        split_command = command.split()
        if not command:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            print("** attribute name missing **")
            return
        elif len(split_command) == 3:
            print("** value missing **")
            return
        else:
            all_dict = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            if key_dict not in all_dict:
                print("** no instance found **")
                return
            else:
                k_upd = split_command[2]
                v_upd = split_command[3]
                all_dict[key_dict].update({k_upd: v_upd.replace('"', '')})
                new_instance = BaseModel(**all_dict[key_dict])
                new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
