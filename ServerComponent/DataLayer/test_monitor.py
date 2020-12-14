from DataLayer.CredibilityScore import get_post_score
from DataLayer.DataSetEntry import SocialMediaDataSetEntry
from DataLayer.DataSetProvider import DataSetProvider
import random


def test_monitor():
    dts_prov = DataSetProvider()
    print("monitor test started")
    param_1 = -3
    param_2 = random.randint(0, 100000)
    param_3 = random.randint(0, 50000)
    param_4 = random.randint(0, 25000)
    param_5 = random.randint(0, 100) / 100
    param_6 = random.randint(0, 100)
    param_7 = get_post_score(param_1, param_2, param_3, param_4, param_5, param_6)
    entry = SocialMediaDataSetEntry(param_1, param_2, param_3, param_4, param_5, param_6, param_7)
    dts_prov.add_data_set_entry(entry)


test_monitor()
