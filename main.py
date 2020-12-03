import repository.accomodation as service
import repository.csv_parser as csv
from service import osm_scraper

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')

townCoordinates = osm_scraper.scrape_page(countyData[0]['Megnevezés'])


print(townCoordinates)

#print(service.loadTable())

