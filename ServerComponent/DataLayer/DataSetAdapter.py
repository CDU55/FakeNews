from DataLayer import DataSetProvider


class DataSetAdapter:
    def __init__(self):
        self.data_set_provider = DataSetProvider()

    def provide_dataset_entries(self):
        raw_data = self.data_set_provider.get_data_set_entries()
        pass