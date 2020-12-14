import {fromLonLat} from "ol/proj";
import {Feature} from "ol";
import {Circle} from "ol/geom";
import Style from "ol/style/Style";
import Stroke from "ol/style/Stroke";
import Fill from "ol/style/Fill";

export function createFeature(data, path){
    const id = data[0];
    const coordinate = data[1];
    const value = data[2];
    const myFeature = new Feature(new Circle(fromLonLat(coordinate), value * 100 * 4000));

    myFeature.setProperties({
        id: id,
        path: path
    });

    const selected_polygon_style = new Style({
        stroke: new Stroke({
            color: 'crimson',
            width: 3
        }),
        fill: new Fill({
            color: 'rgba(0, 0, 255, 0.1)'
        })
    })

    myFeature.setStyle(selected_polygon_style);

    return myFeature;
}
