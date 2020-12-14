from flask import send_file
from main import app, full_dictionary

import io
import matplotlib.pyplot as plt
import numpy as np


@app.route('/correlation/<root>/<csv>')
def csv_correlation(root, csv):
    fig1 = plt.figure(facecolor='#3c4b64')
    ax = fig1.add_subplot(111)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    dataframe = full_dictionary[root][csv].drop(['title', 'id'], axis=1)
    dataframe = dataframe.loc[:, (dataframe != 0).any(axis=0)]
    cax = ax.matshow(dataframe.corr(method='pearson'), cmap='coolwarm')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        attachment_filename='correlation_${root}_${csv}.png',
        mimetype='image/png'
    )


@app.route('/scatter/<root>/<csv>/<column_id>')
def csv_scatter(root, csv, column_id):
    values = full_dictionary[root][csv][column_id].values

    x = np.arange(start=0, stop=len(values), step=1)
    y = values

    plt.scatter(x, y)

    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    # ax.axes.yaxis.set_visible(False)

    plt.grid(True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        attachment_filename='scatter_${root}_${csv}.png',
        mimetype='image/png'
    )
