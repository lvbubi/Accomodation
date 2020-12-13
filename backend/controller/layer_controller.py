from flask import jsonify
from main import app, full_dictionary


@app.route('/percentage/<root>/<csv>/<column>')
def column_percentage(root, csv, column):
    df = full_dictionary[root][csv]
    df[column] = df[column].transform(lambda x: x / x.sum())

    subset = df[['coordinate', 'title', column]]

    return jsonify([tuple(x) for x in subset.to_numpy()])
