import repository.accomodation as service
import repository.csv_parser as csv

townData = csv.parse_package('./teir_adatok_2016/telepules/')

print(townData)

#print(service.loadTable())

