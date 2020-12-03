import repository.accomodation as service
import repository.csv_parser as csv
from service import osm_scraper
import pandas as pd

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')

townCoordinates = osm_scraper.scrape_page(countyData[0]['Megnevezés'])

pd.DataFrame.from_dict(townCoordinates)\
    .to_csv('countyCoordinates.csv')
print(townCoordinates)

#print(service.loadTable())

