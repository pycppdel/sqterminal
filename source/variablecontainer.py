"""
class for storing variables
"""
class VariableContainer:

    def __init__(self):
        #container for variables
        self.saved_variables = {}

    def exists(self, var):
        """
        checks if variable exists
        """
        return (var in self.saved_variables.keys())

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
            self.saved_variables[name] = value
            return True
        except Exception:
            return False

    def delete(self, name):
        """
        deletes variable
        """
        try:
            del self.saved_variables[name]
            return True
        except:
            return False
