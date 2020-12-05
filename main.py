import pandas as pd
import repository.csv_parser as csv
from web_scraping import osm_scraper

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')

county_coordinates = osm_scraper.scrape_page(countyData[0]['title'])


pd.DataFrame.from_dict(county_coordinates)\
    .to_csv('data/countyCoordinates.csv')
