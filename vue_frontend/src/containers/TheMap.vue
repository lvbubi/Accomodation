<template>
  <div ref="map-root" style="width: 100%; height: 100%">
    <TreeView :map="olMap"></TreeView>
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
import TreeView from "@/containers/TreeView";
import 'ol'

export default {
  name: 'TheMap',
  components: {TreeView},
  data: () => ({
    // store OL objects on the component instance
    olMap: {}
  }),

  mounted() {
    const vectorLayer = MarkerService.markerVector();
    this.olMap = new Map({
      // the map will be created using the 'map-root' ref
      target: this.$refs['map-root'],
      layers: [
        // adding a background tiled layer
        new TileLayer({
          source: new OSM() // tiles are served by OpenStreetMap
        }),
        vectorLayer,
        this.$store.state.LayerStore.circleLayer
      ],

      // the map view will initially show the whole world
      view: new View({
        zoom: 7.5,
        center: fromLonLat([18.7887741, 46.4226584]),
        constrainResolution: true
      }),
    });

    //myFeature.setStyle(selected_polygon_style)
    //this.$store.state.circleLayer.getSource().addFeature(myFeature)

    //{"bubblingMouseEvents": true, "color": "crimson", "dashArray": null,
    // "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2,
    // "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0,
    // "radius": 3301, "stroke": true, "weight": 3}
    axios.default.get('http://localhost:5000').then((a) => {

      var result = [];

      for(var i in a.data.coordinate)
        result.push(a.data.coordinate [i]);

      //console.log(a.data.coordinate)
      const features = result.map(coordinate => {
            //console.log(coordinate)
            return new Feature({
              geometry: new Point(fromLonLat(coordinate)),
              style: MarkerService.defaultStyle
            })
          }
      );

      //vectorLayer.getSource().addFeatures(features);
      console.log(a);
    });
  }
}
</script>
