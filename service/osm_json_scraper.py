import json
import urllib.parse
import urllib.request

import service.settings as settings


def scrape_osm_api(towns):
    coordinates = []

    for town in towns:
        url = settings.OSM_API_URL + f'?city={urllib.parse.quote_plus(town)}&country=Hungary&format=geojson'
        print(f"Accessing page at {url} ...")
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            coordinates.append(fetch_coordinate(data['features'], town))

    return coordinates


def fetch_coordinate(features, town):
    if len(features) == 1:
        return town, feature_to_coordinate(features[0])

    for feature in features:
        name = feature['properties']['display_name']
        if name.split(',')[0] == town:
            return town, feature_to_coordinate(feature)


def feature_to_coordinate(feature):
    coordinates = feature['geometry']['coordinates']
    return feature['properties']['display_name'], coordinates
