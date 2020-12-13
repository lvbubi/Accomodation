import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
from service.options import county_path, town_path
from service.coordinate_service import add_coordinates_to_town, add_coordinates_to_county


def parse_data_to_dict():
    return {
        'county': parse_package_to_dict(county_path, add_coordinates_to_county),
        'town': parse_package_to_dict(town_path, add_coordinates_to_town)
    }


def parse_package_to_dict(path, coordinate_function):
    csv_files = get_all_csv(path)

    dictionary = {}

    for filename in csv_files:
        dictionary[filename] = coordinate_function(parse_csv(path + filename))

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

    count_of_meta_lines = column_indexes[1] - column_indexes[0]

    dataframe = dataframe.iloc[: - count_of_meta_lines - 1]
    dataframe.name = column_names[['id', 'title']]
    dataframe.fillna(0, inplace=True)

    return dataframe


def get_all_csv(path):
    all_files = [f for f in listdir(path) if isfile(join(path, f))]
    return list(filter(lambda x: x.endswith('.csv'), all_files))


def fix_column_names(dataframe):
    dataframe.rename(columns={'Megnevezés': 'title'}, inplace=True)
    dataframe.rename(columns={'Kód': 'id'}, inplace=True)
