import numpy as np
# import the modules
import pandas as pd
import pymongo

def loadTable():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    #db = client.datascience
    #collection = db.accomodation

    collection = client.local.datascience

    dataFrame = pd.DataFrame(list(collection.find()), columns=['id', 'county', 'foreign', 'domestic'])

    dataFrame.replace('', np.nan, inplace=True)
    dataFrame.dropna(inplace=True)
    dataFrame.foreign = dataFrame.foreign.astype(int)
    dataFrame.domestic = dataFrame.domestic.astype(int)
    dataFrame.id = dataFrame.id.astype(int)

    return dataFrame

def loadCoordinates():
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    collection = client.local.coordinates

    dataFrame = pd.DataFrame(list(collection.find()), columns=['id', 'longitude', 'latitude'])

    dataFrame.replace('', np.nan, inplace=True)
    dataFrame.dropna(inplace=True)
    dataFrame.id = dataFrame.id.astype(int)

    return dataFrame
