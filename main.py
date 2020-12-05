import repository.csv_parser as csv
from web_scraping import osm_json_scraper
import pandas as pd

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')
for town in townData[0]['title'][1046:]:
    pd.DataFrame(osm_json_scraper.scrape_osm_api([town])) \
        .to_csv('countyCoordinates.csv', mode='a', header=False)
