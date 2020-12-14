from flask import jsonify
from main import app, full_dictionary


@app.route('/percentage/<root>/<csv>/<column>')
def column_percentage(root, csv, column):
    df = full_dictionary[root][csv]
    df[column] = df[column].transform(lambda x: x / x.sum())

    subset = df[['id', 'coordinate', column]]

    return jsonify([tuple(x) for x in subset.to_numpy()])


@app.route('/meta/<root>/<csv>/<column>/<location_id>')
def meta_data(root, csv, column, location_id):
    df = full_dictionary[root][csv]
    subset = df.loc[df['id'] == location_id][['title', 'coordinate', column]]

    sum = df[column].sum()
    value = subset[column].iloc[0]
    title = subset['title'].iloc[0]

    return jsonify({
        'title': title,
        'value': value,
        'sum': sum,
        'probability': value / sum
    })
