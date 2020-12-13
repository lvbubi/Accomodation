import {fromLonLat} from "ol/proj";
import {Feature} from "ol";
import {Circle} from "ol/geom";
import Style from "ol/style/Style";
import Stroke from "ol/style/Stroke";
import Fill from "ol/style/Fill";

export function fuckYeah(arrays){

    let lstOut = []

    arrays.forEach(
        function (a) {
            [0, 1, 2].forEach(
                function (i) {
                    // side-effect on an array outside the function
                    lstOut[i] += a[i];
                }
            );
        }
    );

    return lstOut
}

export function createFeature(coordinate, value, title){

    const centerLongitudeLatitude = fromLonLat(coordinate);


    const myFeature = new Feature(new Circle(centerLongitudeLatitude, 4000));

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
