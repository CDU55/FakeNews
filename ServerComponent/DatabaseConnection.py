
class DatabaseConnection:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DatabaseConnection.__instance == None:
            DatabaseConnection()
        return DatabaseConnection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseConnection.__instance = self