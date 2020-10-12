import numpy as np
# import the modules
import pandas as pd
import pymongo

def loadTable():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.datascience
    collection = db.accomodation

    dataFrame = pd.DataFrame(list(collection.find()), columns=['county', 'foreign', 'domestic'])

    dataFrame.replace('', np.nan, inplace=True)
    dataFrame.dropna(inplace=True)
    dataFrame.foreign = dataFrame.foreign.astype(int)
    dataFrame.domestic = dataFrame.domestic.astype(int)

    return dataFrame
