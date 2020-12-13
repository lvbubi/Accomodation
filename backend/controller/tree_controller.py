from flask import jsonify
from service.options import county_path, town_path
from main import app

import service.csv_parser as parser


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


@app.route('/tree')
def tree_data():
    return jsonify({
        'county': create_column_tree(county_path),
        'town': create_column_tree(town_path)
    })


def create_column_tree(path):
    csv_columns = []
    csv_files = parser.get_all_csv(path)

    for file in csv_files:
        dataframe = parser.parse_csv(path + file)  # type: pd.Dataframe
        dataframe.name.rename(columns={'id': 'title', 'title': 'id'}, inplace=True)

        csv_columns.append({file: dataframe.name.head().to_dict()})

    return csv_columns


@app.route('/<package>/<csv>')
def page(package, csv):
    dataframe = parser.parse_csv('./teir_adatok_2016/' + package + '/' + csv)  # type: pd.Dataframe
    dataframe.name.rename(columns={'id': 'title', 'title': 'id'}, inplace=True)

    return dataframe.name.to_json()
