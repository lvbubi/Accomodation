import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

from model.csv_dataframe import CsvDataFrame


def parse_package(path):

    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    csv_files = list(filter(lambda x: x.endswith('.csv'), all_files))

    package = []

    for filename in csv_files:
        dataframe = pd.read_csv(path + filename)

        column_indexes = np.where(pd.isnull(dataframe['Megnevezés']))[0]

        column_names = dataframe.iloc[column_indexes[0] + 1:column_indexes[1]]


        for column_name in column_names['Megnevezés'].items():
            title = column_names['Kód'][column_name[0]]
            dataframe.rename(columns={column_name[1]: title}, inplace=True)

        csv_dataframe = CsvDataFrame(dataframe, column_names[['Kód', 'Megnevezés']])

        count_of_meta_lines = column_indexes[1] - column_indexes[0]

        package.append(dataframe.iloc[: - count_of_meta_lines - 1])
    return package
