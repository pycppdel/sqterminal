"""
class for handling Sqlite3 requests
"""
import sqlite3

class SqHandler:
    """
    handler for incoming requests
    """
    def __init__(self):
        #making all variables
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        #filemode is initially memory
        #file points to the file the data is stored. If the mode is memory
        #the file is None
        self.filemode = "memory"
        self.file = None

    def execute(self, eingabe, read=False):
        """
        executes the input.

        Gives back answer if read=True

        if Answer is no string, something failed
        """
        backstring = []
        self.cursor.execute(eingabe)
        if not read:
            self.connection.commit()
        else:
            backstring = self.cursor.fetchall()
            return False

        return backstring

    def change_file(self, filename):
        """
        changes file to work with. Databases in other files arent available anymore
        """
        if filename != self.file:
            if filename == "memory":
                self.filemode = "memory"
                self.file = None
                self.change_memory()
            else:
                self.filemode = "file"
                self.file = filename
                self.change_memory()
            return True
        else:
            return False

    def change_memory(self):
        """
        changes connection and cursor
        """
        #making connection and cursor
        self.connection = (sqlite3.connect(":memory:") if self.filemode == "memory"\
        else sqlite3.connect(self.file))
        self.cursor = connection.cursor()
