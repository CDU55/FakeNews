from DataLayer.DataSetAdapter import DataSetAdapter
from DataLayer.DataSetEntry import TwitterDataSetEntry
from DataLayer.DataSetProvider import DataSetProvider
from DataLayer.CredibilityScore import get_post_score
import random

provider = DataSetProvider()


def generate_dummy_data():
    for i in range(0, 10000):
        param_1 = random.randint(0, 500000)
        param_2 = random.randint(0, 1)
        param_3 = random.randint(0, 30000)
        param_4 = random.randint(0, 25000)
        param_5 = random.randint(0, 4000)
        param_6 = random.randint(0, 100000)
        param_7 = random.randint(0, 100) / 100
        param_8 = random.randint(0, 100)
        param_9 = get_post_score(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8)
        entry = TwitterDataSetEntry(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9)
        provider.add_data_set_entry(entry)


def test_dataset(entry_print_number):
    adapter = DataSetAdapter()
    result = adapter.provide_dataset_entries()
    chosen_indexes = set()
    while len(chosen_indexes) < entry_print_number and len(chosen_indexes) < len(result):
        index = random.randint(0, len(result))
        chosen_indexes.add(index)
    for current_index in chosen_indexes:
        entry = result[current_index]
        print("Followers : {}".format(entry.followers_number))
        print("Likes : {}".format(entry.likes_number))
        print("Comments: {}".format(entry.comments_number))
        print("Shares: {}".format(entry.share_number))
        print("Grammar: {}".format(entry.grammar_index))
        print("Subject: {}".format(entry.subject_relevance))
        print("Label: {} ".format(entry.label))
        print(" ")


generate_dummy_data()
