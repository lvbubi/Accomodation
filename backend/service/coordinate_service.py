import os

import pandas as pd
from ast import literal_eval as make_tuple


def add_coordinates_to_county(dataframe):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    county_coordinates = pd.read_csv(current_dir + '/../data/countyCoordinates.csv')

    county_coordinates.coordinate = county_coordinates.coordinate.apply(lambda x: make_tuple(x))

    result = pd.merge(dataframe, county_coordinates, on='title', how='inner')
    result.name = dataframe.name

    return result


def add_coordinates_to_town(dataframe):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    town_coordinates = pd.read_csv(current_dir + '/../data/townCoordinates.csv')
    town_coordinates['county'] = town_coordinates.coordinate.apply(lambda x: extract_country_from_name(x))

    # validation
    invalid_data = town_coordinates[town_coordinates['county'].str.contains('megye') == False]
    if len(invalid_data) != 0:
        raise Exception('county csv contains invalid data', invalid_data)

    town_coordinates.coordinate = town_coordinates.coordinate.apply(lambda x: make_tuple(x)[1])

    result = pd.merge(dataframe, town_coordinates, on='title', how='inner')
    result.name = dataframe.name

    return result


def extract_country_from_name(raw_property):
    name = make_tuple(raw_property)[0]
    return name.split(',')[2]
