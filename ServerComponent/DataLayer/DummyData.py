from DataLayer.DataSetEntry import SocialMediaDataSetEntry
from DataLayer.DataSetProvider import DataSetProvider
import random

provider = DataSetProvider()
followers = ["Very Low", "Low", "Medium", "High", "Very High"]
likes_number = ["Very Low", "Low", "Medium", "High", "Very High"]
comments_number = ["Very Low", "Low", "Medium", "High", "Very High"]
spelling = ["Bad", "Medium", "Good"]
length = ["Very short", "Short", "Medium", "Long", "Very Long"]

for i in range(0, 1000):
    param_1 = random.randint(0, 1000)
    param_2 = random.randint(0, 1000)
    param_3 = random.randint(0, 1000)
    param_4 = random.randint(0, 1000)
    param_5 = random.randint(0, 1000)
    param_6 = random.randint(0, 1)
    entry = SocialMediaDataSetEntry(param_1, param_2, param_3, param_4, param_5, param_6)
    provider.add_data_set_entry(entry)
