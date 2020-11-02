class AnalysisElement:
    def __init__(self, validationResult, validationMessage):
        self.validation_result = validationResult
        self.validation_message = validationMessage

class AnalysisResult:
    def __init__(self):
        self.elements = []

    def add_element(self, element: AnalysisElement):
        self.elements.append(element)


class DataSetEntry:
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

class DataSetEntries:
    def __init__(self):
        self.entries = []

    def add_element(self, entry: DataSetEntry):
        self.entries.append(entry)
