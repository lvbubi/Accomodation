from flask import Flask, jsonify
from flask_cors import CORS
import service.csv_parser as parser
import service.coordinate_service as service
from service.options import county_path, town_path
import pandas as pd

print(town_path)

townData = parser.parse_package(town_path)
countyData = parser.parse_package(county_path)

app = Flask(__name__)
CORS(app)

data = service.add_coordinates_to_town(townData[0])


@app.route('/')
def hello_world():
    return data.to_json()


@app.route('/town')
def town_csv():
    return jsonify({
        'town': parser.get_all_csv(town_path)
    })


@app.route('/county')
def county_csv():
    return jsonify({
        'county': parser.get_all_csv(county_path)
    })


@app.route('/<package>/<csv>')
def page(package, csv):
    dataframe = parser.parse_csv('./teir_adatok_2016/' + package + '/' + csv)  # type: pd.Dataframe
    dataframe.name.rename(columns={'id': 'title', 'title': 'id'}, inplace=True)

    return dataframe.name.to_json()


if __name__ == '__main__':
    app.run()
