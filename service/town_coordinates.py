import pandas as pd
import repository.csv_parser as csv
from service import osm_scraper

townData = csv.parse_package('../teir_adatok_2016/telepules/')

town_coordinates = osm_scraper.scrape_page(townData[0]['Megnevezés'])

pd.DataFrame.from_dict(town_coordinates).to_csv('townCoordinates.csv')
