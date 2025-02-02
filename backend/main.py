from flask import Flask
from flask_cors import CORS

import service.csv_parser as parser
from middleware.reset_plot_middleware import middleware

full_dictionary = parser.parse_data_to_dict()

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.wsgi_app = middleware(app.wsgi_app)

import controller.chart_controller
import controller.layer_controller
import controller.tree_controller

if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False
    app.run()
