import os

from DataLayer import DataSetEntry, DatabaseConnection
from DataLayer.DataSetEntry import SocialMediaDataSetEntry


class DataSetProvider:
    def __init__(self):
        pass

    def edit_data_set_entry(self, entry):
        pass

    def delete_data_set_entry(self, entry):
        pass

    def add_data_set_entry(self, entry: SocialMediaDataSetEntry):
        conn = DatabaseConnection.DatabaseConnection.getInstance()
        id = conn.execute('SELECT MAX(Id) FROM SocialMediaPosts').fetchone()[0]
        params = (
            id + 1, entry.followers_number, entry.likes_number, entry.comments_number, entry.spelling, entry.length,
            entry.label)
        query = "INSERT INTO SocialMediaPosts VALUES (?,?,?,?,?,?,?)"
        conn.execute(query, params)
        conn.commit()

    def get_data_set_entries(self):
        conn = DatabaseConnection.DatabaseConnection.getInstance()
        return conn.execute("Select * FROM SocialMediaPosts")

