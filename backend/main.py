from flask import Flask, jsonify
from flask_cors import CORS
import service.csv_parser as csv
import service.coordinate_service as service
from service.options import county_path, town_path

print(town_path)

townData = csv.parse_package(town_path)
countyData = csv.parse_package(county_path)

app = Flask(__name__)
CORS(app)

data = service.add_coordinates_to_town(townData[0])


@app.route('/')
def hello_world():
    return data.to_json()


@app.route('/town')
def town_csv():
    return jsonify({
        'telepules': csv.get_all_csv(town_path)
    })


@app.route('/county')
def county_csv():
    return jsonify({
        'megye': csv.get_all_csv(county_path)
    })


if __name__ == '__main__':
    app.run()
