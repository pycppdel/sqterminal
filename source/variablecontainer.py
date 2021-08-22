"""
class for storing variables
"""
class VariableContainer:

    def __init__(self):
        #container for variables
        self.saved_variables = {}
        #for changing variables
        self.variable_operations = {

        "string": str,
        "int": int,
        "byte": byte,
        }

    def exists(self, var):
        """
        checks if variable exists
        """
        return (var in self.variables.keys())

    def get_var(self, name):
        """
        gives back value of var
        """
        return self.saved_variables[name]

    def make_var(self, name, value):
        """
        makes variable
        """
        try:
            self.saved_variables[name] = self.variable_operations[value]
            return True
        except Exception:
            return False
