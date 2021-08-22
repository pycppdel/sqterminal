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
        return "RUNNING"

    def exit(self):
        """
        exits running state
        """
        return "STOPPED"

    def make_variable(name, value):
        pass

    def change_file_mode(self, name):
        pass

    def execute(self, eingabe):
        """
        executes function
        """
        try:
            readen = False
            upe = eingabe.lowercase()
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
        pattern = r"\$([a-zA-Z]*)"
        found = re.findall(pattern, eingabe)
        asked = (len(re.findall(r"(\$[a-zA-Z]+ ?)", eingabe)) == len(re.findall("\$", eingabe)))
        if found:
            for el in found:
                if self.variablecontainer.exists(str(el)):
                    eingabe = eingabe.replace(str("$"+el), self.variablecontainer.get_var(str(el)))
        return eingabe, asked

    def add_variable(self, typ, name, value):
        """
        Adds a variable
        """
        typ = self.variablecontainer.variable_operations[typ]
        self.variablecontainer.make_var(name, typ(value))
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
