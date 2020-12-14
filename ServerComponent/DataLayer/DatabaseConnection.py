import sqlite3
import os


class DatabaseConnection:

    def getInstance(self):
        path = os.path.join(os.path.dirname(__file__), "dataset.db")
        #path = os.path.realpath("dataset.db")
        return sqlite3.connect(path)
