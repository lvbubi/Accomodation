import repository.accomodation as service
import repository.csv_parser as csv
from service import osm_scraper
from service import osm_json_scraper
import pandas as pd

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')

townCoordinates = pd.DataFrame(osm_json_scraper.scrape_osm_api(townData[0]['Megnevezés']))

pd.DataFrame.from_dict(townCoordinates)\
   .to_csv('countyCoordinates.csv')
print(townCoordinates)

