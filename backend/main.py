import io

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, jsonify, send_file
from flask_cors import CORS

import service.coordinate_service as service
import service.csv_parser as parser
from service.options import county_path, town_path

print(town_path)

townData = parser.parse_package(town_path)
townDictionary = parser.parse_package_to_dict(town_path)
countyData = parser.parse_package(county_path)

full_dictionary = parser.parse_data_to_dict()

app = Flask(__name__)
CORS(app)

data = service.add_coordinates_to_town(townData[0])


@app.route('/percentage/<root>/<csv>/<column>')
def column_percentage(root, csv, column):
    df = full_dictionary[root][csv]
    df = service.add_coordinates_to_town(df)
    df[column] = df[column].transform(lambda x: x / x.sum())

    subset = df[['coordinate', 'title', column]]

    return jsonify([tuple(x) for x in subset.to_numpy()])


@app.route('/correlation/<root>/<csv>')
def csv_correlation(root, csv):
    fig1 = plt.figure(facecolor='#3c4b64')
    ax = fig1.add_subplot(111)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    dataframe = full_dictionary[root][csv].drop(['title', 'id'], axis=1)
    print(dataframe)

    cax = ax.matshow(dataframe.corr(method='pearson'), cmap='coolwarm')
    # ax.xticklabels=iris[1:4]
    #fig1.colorbar(cax)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        attachment_filename='${root}/${csv}.png',
        mimetype='image/png'
    )


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


if __name__ == '__main__':
    # app.config['JSON_AS_ASCII'] = False
    app.run()
