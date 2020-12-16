from flask import send_file
from main import app, full_dictionary

import io
import matplotlib.pyplot as plt
import numpy as np


@app.route('/correlation/<c_type>/<root>/<csv>')
def csv_correlation(c_type, root, csv):
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    dataframe = full_dictionary[root][csv].drop(['title', 'id'], axis=1)
    dataframe = dataframe.loc[:, (dataframe != 0).any(axis=0)]
    cax = ax.matshow(dataframe.corr(method=c_type), cmap='coolwarm')

    return create_response(f'correlation_${root}_${csv}.png')


@app.route('/heatmap/county/<csv>')
def csv_heatmap(root, csv):

    dataframe = get_data_columns(root, csv)
    dataframe = dataframe.loc[:, (dataframe != 0).any(axis=0)]

    plt.imshow(dataframe.to_numpy(), cmap='hot', interpolation='nearest')

    return create_response(f'heatmap_${root}_${csv}.png')


@app.route('/scatter/<root>/<csv>/<column_id>')
def csv_scatter(root, csv, column_id):
    values = full_dictionary[root][csv][column_id].values

    x = np.arange(start=0, stop=len(values), step=1)
    y = values

    plt.scatter(x, y)

    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(True)

    return create_response(f'scatter_${root}_${csv}.png')


def create_response(name):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        attachment_filename=name,
        mimetype='image/png'
    )


def get_data_columns(root, csv):
    dataframe = full_dictionary[root][csv]

    return dataframe[dataframe.name['title']]
