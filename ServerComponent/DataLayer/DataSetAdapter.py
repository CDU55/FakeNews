from DataLayer import DataSetProvider
from DataLayer.DataSetEntry import SocialMediaDataSetEntry


class DataSetAdapter:
    def __init__(self):
        self.data_set_provider = DataSetProvider.DataSetProvider()

    def provide_dataset_entries(self):
        raw_data = self.data_set_provider.get_data_set_entries()
        entries = []
        for entry in raw_data:
            current_entry = SocialMediaDataSetEntry(entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
            entries.append(current_entry)
        return entries

