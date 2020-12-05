import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join


def parse_package(path):
    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    csv_files = list(filter(lambda x: x.endswith('.csv'), all_files))

    package = []

    for filename in csv_files:
        dataframe = pd.read_csv(path + filename)
        fix_column_names(dataframe)

        column_indexes = np.where(pd.isnull(dataframe['title']))[0]
        column_names = dataframe.iloc[column_indexes[0] + 1:column_indexes[1]]
        # map_column_names(dataframe, column_names)

        count_of_meta_lines = column_indexes[1] - column_indexes[0]

        dataframe = dataframe.iloc[: - count_of_meta_lines - 1]
        dataframe.name = column_names[['id', 'title']]
        package.append(dataframe)

    return package


def map_column_names(dataframe, column_names):
    for column_name in column_names['title'].items():
        title = column_names['Kód'][column_name[0]]
        dataframe.rename(columns={column_name[1]: title}, inplace=True)
        dataframe.rename(columns={f'SUM({column_name[1]})': title}, inplace=True)


def fix_column_names(dataframe):
    dataframe.rename(columns={'Megnevezés': 'title'}, inplace=True)
    dataframe.rename(columns={'Kód': 'id'}, inplace=True)
