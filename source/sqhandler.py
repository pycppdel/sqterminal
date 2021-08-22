"""
class for handling Sqlite3 requests
"""
import sqlite3

class SqHandler:
    """
    handler for incoming requests
    """
    def __init__(self):

        #file is a prerequesite for comnparing file in the cgange method
        self.file = ""
        self.change_file("memory")

    def execute(self, eingabe, read=False):
        """
        executes the input.

        Gives back answer if read=True

        if Answer is no string, something failed
        """
        #executing
        self.cursor.execute(eingabe)
        #trying to commit
        try:
            self.connection.commit()
        except Exception:
            #something went wrong: rollback + failure message
            self.connection.rollback()
            return False
        #commit happened:
        if read:
            #if it was SELECT statement
            backstring = self.cursor.fetchall()
            #returning selected items
            return backstring
        else:
            #everything clear: return true
            return True

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
        self.cursor = self.connection.cursor()
