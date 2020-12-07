from DataLayer import DataSetProvider, DataCategories
from DataLayer.DataSetEntry import TwitterDataSetEntry
import numpy as np

from DataLayer.aspects import my_decorator_exit_db


class DataSetAdapter:
    def __init__(self):
        self.data_set_provider = DataSetProvider.DataSetProvider()
        self.categories = 8

    @my_decorator_exit_db
    def provide_dataset_entries(self):
        raw_data = self.data_set_provider.get_data_set_entries()
        entries = []
        for entry in raw_data:
            current_entry = TwitterDataSetEntry(entry[1], entry[2], entry[3], entry[4], entry[5], entry[6],
                                                entry[7], entry[8],entry[9])
            entries.append(current_entry)
        return entries

    def convert_to_training_datasets(self):
        db_entries = self.provide_dataset_entries()
        characteristics = np.zeros((len(db_entries), self.categories))
        labels = np.zeros(len(db_entries))
        for index, post in enumerate(db_entries):
            characteristics[index, 0] = post.followers_number
            characteristics[index, 1] = post.verified
            characteristics[index, 2] = post.tweets_number
            characteristics[index, 3] = post.retweets
            characteristics[index, 4] = post.quote_tweets
            characteristics[index, 5] = post.likes_number
            characteristics[index, 6] = post.grammar_index
            characteristics[index, 7] = post.subject_relevance
            labels[index] = post.label
        return characteristics, labels

    def convert_to_predict_data(self, data: TwitterDataSetEntry):
        predict_data = np.zeros(self.categories)
        predict_data[0] = DataCategories.get_followers_category(data.followers_number)
        predict_data[1] = data.verified
        predict_data[2] = DataCategories.get_tweets_number_category(data.tweets_number)
        predict_data[3] = DataCategories.get_shares_category(data.retweets)
        predict_data[4] = DataCategories.get_quote_tweets_category(data.quote_tweets)
        predict_data[5] = DataCategories.get_likes_category(data.likes_number)
        predict_data[6] = DataCategories.get_grammar_index_category(data.grammar_index)
        predict_data[7] = DataCategories.get_subject_relevance_index_category(data.subject_relevance)
        return predict_data
