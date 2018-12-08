import pandas as pd
from sklearn.preprocessing import LabelEncoder


class Reader:

    def __init__(self, name):
        self.name = name
        self.dataset = self.load_file()
        self.dataset = self.dataset.iloc[:, :].values

    # Should eventually handle more than just csv files
    def load_file(self):
        return pd.read_csv(self.name)

    def getFile(self):
        return self.dataset

    def get_headers(self):
        return self.dataset.head(0)

    # Will try to improve in future to work
    """def processHeaders(self):
        headers = self.getHeaders()
        invalid_headers = []
        valid_headers = []
        for header in headers:
            if isinstance(header, str):
                valid_headers.append(header)
            else:
                invalid_headers.append(header)"""

    def process_data(self):
        invalid_indexes = []
        i = 0
        for data in self.dataset.tolist()[0]:
            if isinstance(data, str):
                invalid_indexes.append(i)
            i += 1
        return invalid_indexes

    def encode_data(self):
        label_encoder_x = LabelEncoder()
        for index in self.process_data():
            self.dataset[:, index] = label_encoder_x.fit_transform(self.dataset[:, index])
        return self.dataset

    def get_processed_data(self):
        return self.encode_data()

