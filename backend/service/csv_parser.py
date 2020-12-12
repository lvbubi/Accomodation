import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join


def parse_package_to_dict(path):
    csv_files = get_all_csv(path)

    dictionary = {}

    for filename in csv_files:
        dictionary[filename] = parse_csv(path + filename)

    return dictionary


def parse_package(path):
    csv_files = get_all_csv(path)

    package = []

    for filename in csv_files:
        package.append(parse_csv(path + filename))

    return package


def parse_csv(path):
    dataframe = pd.read_csv(path)
    fix_column_names(dataframe)

    column_indexes = np.where(pd.isnull(dataframe['title']))[0]
    column_names = dataframe.iloc[column_indexes[0] + 1:column_indexes[1]]
    # map_column_names(dataframe, column_names)

    count_of_meta_lines = column_indexes[1] - column_indexes[0]

    dataframe = dataframe.iloc[: - count_of_meta_lines - 1]
    dataframe.name = column_names[['id', 'title']]

    return dataframe


def get_all_csv(path):
    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    return list(filter(lambda x: x.endswith('.csv'), all_files))


def map_column_names(dataframe, column_names):
    for column_name in column_names['title'].items():
        title = column_names['Kód'][column_name[0]]
        dataframe.rename(columns={column_name[1]: title}, inplace=True)
        dataframe.rename(columns={f'SUM({column_name[1]})': title}, inplace=True)


def fix_column_names(dataframe):
    dataframe.rename(columns={'Megnevezés': 'title'}, inplace=True)
    dataframe.rename(columns={'Kód': 'id'}, inplace=True)
