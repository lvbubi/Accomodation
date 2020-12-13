from flask import send_file
from main import app, full_dictionary

import io
import matplotlib.pyplot as plt


@app.route('/correlation/<root>/<csv>')
def csv_correlation(root, csv):
    fig1 = plt.figure(facecolor='#3c4b64')
    ax = fig1.add_subplot(111)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    dataframe = full_dictionary[root][csv].drop(['title', 'id'], axis=1)
    print(dataframe)

    cax = ax.matshow(dataframe.corr(method='pearson'), cmap='coolwarm')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        attachment_filename='${root}/${csv}.png',
        mimetype='image/png'
    )
