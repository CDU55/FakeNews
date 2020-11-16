from DataLayer import DataSetProvider
from DataLayer.DataSetEntry import SocialMediaDataSetEntry
import numpy as np
from Analysers.NaiveBayes import NaiveBayes


class DataSetAdapter:
    def __init__(self):
        self.data_set_provider = DataSetProvider.DataSetProvider()
        self.notations = {
            "followers_number": {"Very Low": 1, "Low": 2, "Medium": 3, "High": 4, "Very High": 5},
            "likes_number": {"Very Low": 1, "Low": 2, "Medium": 3, "High": 4, "Very High": 5},
            "comments_number": {"Very Low": 1, "Low": 2, "Medium": 3, "High": 4, "Very High": 5},
            "spelling": {"Bad": 1, "Medium": 2, "Good": 3},
            "length": {"Very short": 1, "Short": 2, "Medium": 3, "Long": 4, "Very Long": 5}
        }

    def provide_dataset_entries(self):
        raw_data = self.data_set_provider.get_data_set_entries()
        entries = []
        for entry in raw_data:
            current_entry = SocialMediaDataSetEntry(entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
            entries.append(current_entry)
        return entries

    def convert_to_training_datasets(self):
        db_entries = self.provide_dataset_entries()
        characteristics = np.zeros((len(db_entries), len(self.notations)))
        labels = np.zeros(len(db_entries))
        for index, post in enumerate(db_entries):
            characteristics[index, 0] = self.notations["followers_number"][post.followers_number]
            characteristics[index, 1] = self.notations["likes_number"][post.likes_number]
            characteristics[index, 2] = self.notations["comments_number"][post.comments_number]
            characteristics[index, 3] = self.notations["spelling"][post.spelling]
            characteristics[index, 4] = self.notations["length"][post.length]
            labels[index] = post.label
        return characteristics, labels

    def convert_to_predict_data(self, data: SocialMediaDataSetEntry):
        predict_data = np.zeros(len(self.notations))
        predict_data[0] = self.notations["followers_number"][data.followers_number]
        predict_data[1] = self.notations["likes_number"][data.likes_number]
        predict_data[2] = self.notations["comments_number"][data.comments_number]
        predict_data[3] = self.notations["spelling"][data.spelling]
        predict_data[4] = self.notations["length"][data.length]
        return predict_data



