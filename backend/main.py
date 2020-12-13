from flask import Flask
from flask_cors import CORS

import service.csv_parser as parser
from service.options import county_path, town_path

townData = parser.parse_package(town_path)
townDictionary = parser.parse_package_to_dict(town_path)
countyData = parser.parse_package(county_path)

full_dictionary = parser.parse_data_to_dict()

app = Flask(__name__)
CORS(app)
import controller.chart_controller
import controller.layer_controller
import controller.tree_controller

if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False
    app.run()
