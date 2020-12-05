import pandas as pd
from ast import literal_eval as make_tuple


def add_coordinates_to_county(dataframe):
    town_coordinates = pd.read_csv('../data/countyCoordinates.csv')

    town_coordinates.coordinate = town_coordinates.coordinate.apply(lambda x: make_tuple(x))
    return pd.merge(dataframe, town_coordinates, on='title', how='inner')


def add_coordinates_to_town(dataframe):
    town_coordinates = pd.read_csv('../data/townCoordinates.csv')

    town_coordinates.coordinate = town_coordinates.coordinate.apply(lambda x: make_tuple(x)[1])
    return pd.merge(dataframe, town_coordinates, on='title', how='inner')
