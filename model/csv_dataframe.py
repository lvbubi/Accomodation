import pandas as pd


class CsvDataFrame:
    def __init__(self, dataframe, columns):
        self.dataframe = dataframe  # type: pd.DataFrame
        self.columns = columns  # type: list
