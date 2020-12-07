import os

from DataLayer import DataSetEntry, DatabaseConnection, DatabaseOperations
from DataLayer.DataSetEntry import TwitterDataSetEntry
from Utils.LoggingAspect import logging_aspect


class DataSetProvider:
    def __init__(self):
        pass

    @logging_aspect
    def add_data_set_entry(self, entry: TwitterDataSetEntry):
        next_id = DatabaseOperations.get_next_id()
        params = (
            next_id + 1, entry.followers_number, entry.verified, entry.tweets_number, entry.retweets, entry.quote_tweets, entry.likes_number, entry.grammar_index, entry.subject_relevance,entry.label)
        DatabaseOperations.insert_entry(params)

    def get_data_set_entries(self):
        return DatabaseOperations.get_all()

