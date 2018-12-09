from collections import defaultdict

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy import stats
import numpy as np


def get_string_index(list_of_pairs, string):
    for pair in list_of_pairs:
        if pair[1] == string:
            return pair[0]
    return -1


class Reader:

    def __init__(self, name):
        self.name = name
        self.dataset = self.load_file()
        self.headers_dict = defaultdict(str)
        self.get_headers()
        """
        self.encode_dict = defaultdict(list)
        self.encode_strings()
        self.y_matrix = [[]]
        self.x_matrix = [[]]"""

    # Should eventually handle more than just csv files
    def load_file(self):
        return pd.read_csv(self.name)

    def getFile(self):
        return self.dataset

    def get_headers(self):
        i = 0
        for header in self.dataset.head(0):
            self.headers_dict[i] = header
            i += 1

    def get_headers_names(self):
        return list(self.headers_dict.values())

    def get_header_col(self, name):
        for number, names in self.headers_dict.items():
            if names == name:
                return number
        return -1

    def process_headers(self):
        headers = self.get_headers()
        invalid_headers = []
        valid_headers = []
        for header in headers:
            if isinstance(header, str):
                valid_headers.append(header)
            else:
                invalid_headers.append(header)

        return {valid_headers, invalid_headers}

    def encode_strings(self):
        for index in self.find_string_data():
            for row in self.dataset:
                i = 0
                for data in row:
                    if i == index:
                        value = self.encode_dict[index]
                        if len(value) > 0:
                            if (self.get_encode_pair(index, data), data) not in self.encode_dict[index]:
                                value.append((self.get_encode_pair(index, data), data))
                        else:
                            value.append((self.get_encode_pair(index, data), data))
                    i += 1

    def get_encode_pair(self, index, data):

        list_of_pairs = self.encode_dict.get(index, )
        if len(list_of_pairs) == 0:
            return 0
        else:
            string_index = get_string_index(list_of_pairs, data)
            if string_index == -1:
                return len(list_of_pairs)
            else:
                return string_index

    def find_string_data(self):
        invalid_indexes = []
        i = 0
        for data in self.dataset.tolist()[0]:
            if isinstance(data, str):
                invalid_indexes.append(i)
            i += 1
        return invalid_indexes

    def encode_data(self):
        label_encoder_x = LabelEncoder()
        for index in self.find_string_data():
            self.dataset[:, index] = label_encoder_x.fit_transform(self.dataset[:, index])
        return self.dataset

    def get_processed_data(self):
        return self.encode_data()

    def get_string(self, index, number):
        index_list = self.encode_dict.get(index, "")
        for pair in index_list:
            if pair[0] == number:
                return pair[1]
        return ""

    def get_number(self, index, string):
        index_list = self.encode_dict.get(index, "")
        for pair in index_list:
            if pair[1] == string:
                return pair[0]
        return -1

    def set_Y(self, y_index):
        #print(self.dataset)
        #print("im removing y_index {}".format(y_index))
        self.y_matrix = [row[y_index] for row in self.dataset]
        self.x_matrix = np.delete(self.dataset, 1, y_index)

    def get_y_matrix(self):
        return self.y_matrix

    def get_x_matrix(self):
        return self.x_matrix