<template>
  <div ref="map-root"
       style="width: 100%; height: 100%">
  </div>
</template>

<script>
import View from 'ol/View'
import Map from 'ol/Map'
import TileLayer from 'ol/layer/Tile'
import 'ol/ol.css'
import * as axios from "axios";
import {Feature} from "ol";
import {Point} from "ol/geom";
import {fromLonLat} from "ol/proj";
import OSM from "ol/source/OSM";
import MarkerService from "@/containers/MarkerService";

export default {
  name: 'TheMap',
  components: {},
  data: () => ({
    // store OL objects on the component instance
    olMap: {}
  }),

  mounted() {
    const vectorLayer = MarkerService.markerVector();

    const map = new Map({
      // the map will be created using the 'map-root' ref
      target: this.$refs['map-root'],
      layers: [
        // adding a background tiled layer
        new TileLayer({
          source: new OSM() // tiles are served by OpenStreetMap
        }),
        vectorLayer
      ],

      // the map view will initially show the whole world
      view: new View({
        zoom: 0,
        center: [0, 0],
        constrainResolution: true
      }),
    });

    this.olMap = map;

    axios.default.get('http://localhost:5000').then((a) => {

      var result = [];

      for(var i in a.data.coordinate)
        result.push(a.data.coordinate [i]);

      console.log(a.data.coordinate)
      const features = result.map(coordinate => {
            console.log(coordinate)
            return new Feature({
              geometry: new Point(fromLonLat(coordinate)),
              style: MarkerService.defaultStyle
            })
          }
      );

      vectorLayer.getSource().addFeatures(features);
      console.log(a);
    });
  }
}
</script>
