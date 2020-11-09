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
        cursor = conn.cursor()
        id = cursor.execute('SELECT MAX(Id) FROM SocialMediaPosts').fetchone()
        query="INSERT INTO SocialMediaPosts VALUES (1,'{}','{}','{}','{}','{}',{})".format( entry.followers_number,
                                                                                          entry.likes_number,
                                                                                          entry.comments_number,
                                                                                          entry.spelling, entry.length,
                                                                                          entry.label)
        cursor.execute(query)

    def get_data_set_entries(self):
        pass


provider = DataSetProvider()
element = SocialMediaDataSetEntry("High", "VeryHigh", "Medium", "Good", "Long", 1)
provider.add_data_set_entry(element)
