#!/usr/bin/python3
"""Console module"""

import cmd
import json
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

CLASSES = {
    "Amenity": Amenity,
    "BaseModel": BaseModel, 
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class HBNBCommand(cmd.Cmd):
    """HBNB console command interpreter"""
    
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """Exits console"""
        return True
    
    def emptyline(self):
        """Overrides default emptyline method"""
        pass
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_create(self, arg):
        """Creates a new instance, saves it to storage"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in CLASSES:
            print("** class doesn't exist **")
            return
            
        new_obj = CLASSES[arg]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = parse(arg)
        if not args:
            return
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
            
        obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in obj:
            print("** no instance found **")
            return
        print(obj[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = parse(arg)
        if not args:
            return
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
            
        obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in obj:
            print("** no instance found **")
            return
            
        del obj[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances"""
        obj = storage.all()
        if not arg:
            print([str(v) for v in obj.values()])
        elif arg not in CLASSES:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in obj.items() if isinstance(v, CLASSES[arg])])

    def do_update(self, arg):
        """Update an instance"""
        args = parse(arg)
        if not args:
            return
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
            
        obj = storage.all()  
        key = "{}.{}".format(args[0], args[1])
        if key not in obj:
            print("** no instance found **")
            return
            
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
            
        attr, value = args[2], args[3]
        setattr(obj[key], attr, value)
        obj[key].save()
        
    def do_count(self, arg):
        """Retrieve number of instances of a class"""
        obj = storage.all()
        if not arg:
            print(len(obj))
        elif arg not in CLASSES:
            print("** class doesn't exist **")
        else:
            print(len([v for k, v in obj.items() if isinstance(v, CLASSES[arg])]))
            
    def default(self, line):
        """Overrides default method"""
        pass
        
def parse(arg):
    """Parses argument string into list"""
    arg_list = arg.split()
    arg_list = arg_list if len(arg_list) > 1 else []
    return arg_list
  
if __name__ == "__main__":
    HBNBCommand().cmdloop()
