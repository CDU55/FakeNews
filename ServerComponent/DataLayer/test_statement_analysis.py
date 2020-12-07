import random

from DataLayer.CredibilityScore import get_post_score
from DataLayer.DataSetEntry import TwitterDataSetEntry
from DataLayer.DataSetProvider import DataSetProvider

param_1 = random.randint(0, 500000)
param_2 = random.randint(0, 1)
param_3 = random.randint(0, 30000)
param_4 = random.randint(0, 25000)
param_5 = random.randint(0, 4000)
param_6 = random.randint(0, 100000)
param_7 = random.randint(0, 100) / 100
param_8 = random.randint(0, 100)
param_9 = get_post_score(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8)
param_7 = None
entry = TwitterDataSetEntry(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9)
provider = DataSetProvider()
provider.add_data_set_entry(entry)
