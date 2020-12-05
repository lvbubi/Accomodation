import numpy as np
import pandas as pd
import pymongo
import repository.settings as settings

def loadTable():
    client = pymongo.MongoClient(settings.DATABASE_URI)
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
    client = pymongo.MongoClient(settings.DATABASE_URI)

    collection = client.local.coordinates

    dataFrame = pd.DataFrame(list(collection.find()), columns=['id', 'longitude', 'latitude'])

    dataFrame.replace('', np.nan, inplace=True)
    dataFrame.dropna(inplace=True)
    dataFrame.id = dataFrame.id.astype(int)

    return dataFrame
