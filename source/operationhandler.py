"""
functions for executing in terminal
"""
import colorama
import re

colorama.init()

from variablecontainer import VariableContainer
from sqhandler import SqHandler

class OperationHandler:

    def __init__(self, varc):
        """
        container linked to terminal
        """
        self.variablecontainer = varc
        self.sqHandler = SqHandler()

    def welcome(self):
        """
        prints welcome text
        """
        print()
        print(colorama.Fore.CYAN+"-"*30)
        print("{:^30}".format("SqTerminal Version 1.0"))
        print("-"*30)
        print(colorama.Fore.RESET)

    def help(self):
        """
        prints help text
        """
        print(colorama.Fore.MAGENTA)
        print()
        print("List of commands and explanation")
        print()
        ce = {
        "help": "prints a list with commands and their use",
        "exit": "leaves the program",
        "[a] = [b]": "sets variable a to value b. Its value can be read by $a",
        "$a": "reads and replaces variable a's value. If it's the only statement the value of a will be prompted",
        "del a": "deletes variable a",
        "show -v[variables]": "shows all variables and their values",
        ":$a": "Auxiliary statement. If a command in variable a is stored, and you type $a, the value will be prompted. But if you type :$a, a will be executed",
        "file = name": "sets the current database file to name, memory sets it to session memory",
        "ANY OTHER STATEMENT": "sql statements like SELECT, CREATE TABLE usw. will be executed automatically",
        }
        print("-"*30)
        for el in ce:
            print("{:<20} | {:^10} ".format(el, ce[el]))
        print("-"*30)
        print(colorama.Fore.RESET)
        return "RUNNING"

    def exit(self):
        """
        exits running state
        """
        return "STOPPED"


    def change_file_mode(self, name):
        """
        changes file mode to name
        """
        if not self.sqHandler.change_file(name):
            print(colorama.Fore.RED)
            print("ERROR: File is still selected.\nType 'help' to see help")
            print(colorama.Fore.RESET)
        return "RUNNING"


    def execute(self, eingabe):
        """
        executes function
        """
        try:
            readen = False
            upe = eingabe.lower()
            if "select" in upe:
                readen = True
            back = self.sqHandler.execute(eingabe, readen)
            if type(back) == list:
                print(colorama.Fore.GREEN)
                print(back)
                print(colorama.Fore.RESET)
        except Exception:
            #printing error message
            print(colorama.Fore.RED)
            print("ERROR: Invalid execution input.\nType 'help' to see help")
            print(colorama.Fore.RESET)
        return "RUNNING"



    def substitute_variables(self, eingabe):
        """
        substitutes variables
        """
        only_show = False
        show_pattern = r"^\$([a-zA-Z]+)$"
        show_found = re.search(show_pattern, eingabe)
        if bool(show_found):
            only_show = self.variablecontainer.exists(show_found.groups(0)[0])
        pattern = r"\$([a-zA-Z]*)"
        found = re.findall(pattern, eingabe)
        if found:
            for el in found:
                if self.variablecontainer.exists(str(el)):
                    eingabe = eingabe.replace(str("$"+el), self.variablecontainer.get_var(str(el)))
        return eingabe, only_show

    def add_variable(self, name, value):
        """
        Adds a variable
        """
        self.variablecontainer.make_var(name, value)
        return "RUNNING"

    def show_variables(self):
        """
        shows variables
        """
        print(colorama.Fore.MAGENTA)
        for el in self.variablecontainer.saved_variables:
            print("["+str(el)+"] = "+str(self.variablecontainer.saved_variables[el]))
        print(colorama.Fore.RESET)
        return "RUNNING"

    def delete_variable(self, name):
        """
        deletes variable
        """
        if not self.variablecontainer.delete(name):
            print(colorama.Fore.RED)
            print("ERROR: No variable with this name.\nType 'help' to see help")
            print(colorama.Fore.RESET)

        return "RUNNING"
