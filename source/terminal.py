"""
class for I/O
"""
import re
from sqhandler import SqHandler
from variablecontainer import VariableContainer
from operationhandler import OperationHandler
import colorama

class TerminalHandler:
    def __init__(self):
        """
        Handler for everything
        """
        self.variablecontainer = VariableContainer()
        self.write_operation_performed = False
        self.callback_data = "RUNNING"
        self.read_operation_performed = False
        self.operationhandler = OperationHandler(self.variablecontainer)
        self.only_show = False

    def run(self):
        self.operationhandler.welcome()
        #while is running
        while self.callback_data == "RUNNING":

            #getting input
            eingabe = input(">")


            eingabe, self.only_show = self.test_for_variables(eingabe)

            self.callback_data= self.invoke_operation(eingabe)


    def invoke_operation(self, eingabe):
        """
        extracting infos
        """
        #regular expressions
        variable_make = r"^([a-zA-Z]*) = ([a-zA-Z0-9 ]+)$"
        #for destroying
        variable_destroy = r"^del [-v ]?([a-zA-Z]*)$"
        #file_change
        file_change = r"^[Ff]ile *= *([\w|\d|\.]*)$"

        #bool
        variable_inside = re.search(variable_make, eingabe)
        variable_delete_inside = re.search(variable_destroy, eingabe)
        file_change_happend = re.search(file_change, eingabe)
        #exiting
        if eingabe == "exit":
            function = self.operationhandler.exit
        elif self.only_show:
            print(colorama.Fore.MAGENTA)
            print(eingabe)
            print(colorama.Fore.RESET)
            function = lambda: "RUNNING"
        elif eingabe == "help":
            function = self.operationhandler.help
        elif variable_inside:
            #making the variable
            name, value = variable_inside.groups(0)[0], variable_inside.groups(0)[1]
            #making variable
            function = lambda: self.operationhandler.add_variable(name, value)
        elif file_change_happend:
            #changing the file
            filename = file_change_happend.groups(0)[0]
            print(filename)
            function = lambda: self.operationhandler.change_file_mode(filename)
        elif eingabe == "show variables" or eingabe == "show -v":
            function = self.operationhandler.show_variables
        elif variable_delete_inside:
            function = lambda: self.operationhandler.delete_variable(variable_delete_inside.groups(0)[0])
        elif not eingabe:
            function = lambda: "RUNNING"
        else:
            if eingabe.startswith(":"):
                eingabe = eingabe.split(":")[1]
            function = lambda: self.operationhandler.execute(eingabe)

        return function()

    def test_for_variables(self, eingabe):
        """
        tests for and changes variables
        """
        return self.operationhandler.substitute_variables(eingabe)
