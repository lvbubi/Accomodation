from flask import Flask
import repository.csv_parser as csv
import service.coordinate_service as service

townData = csv.parse_package('./teir_adatok_2016/telepules/')
countyData = csv.parse_package('./teir_adatok_2016/megye/')

app = Flask(__name__)

data = service.add_coordinates_to_county(countyData[0])


@app.route('/')
def hello_world():
    return data.to_json()


if __name__ == '__main__':
    app.run()
