import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

from model.csv_dataframe import CsvDataFrame


def parse_package(path):

    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    csv_files = list(filter(lambda x: x.endswith('.csv'), all_files))

    print(csv_files)

    package = []

    for filename in csv_files:
        dataframe = pd.read_csv(path + filename, encoding='latin-1')

        column_indexes = np.where(pd.isnull(dataframe['Megnevezés']))[0]

        column_names = dataframe.iloc[column_indexes[0] + 1:column_indexes[1]]

        csv_dataframe = CsvDataFrame(dataframe, column_names)

        package.append(csv_dataframe)
        # print(csv_dataframe.columns['Kód'])

    return package
