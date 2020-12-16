<template>
  <div ref="map-root" style="width: 100%; height: 100%">
    <TreeView :map="olMap"></TreeView>
    <FeaturePopup :map="olMap"></FeaturePopup>
  </div>
</template>

<script>
import View from 'ol/View'
import Map from 'ol/Map'
import TileLayer from 'ol/layer/Tile'
import 'ol/ol.css'
import {fromLonLat} from "ol/proj";
import OSM from "ol/source/OSM";
import MarkerService from "@/containers/MarkerService";
import TreeView from "@/containers/treeview/TreeView";
import 'ol'
import FeaturePopup from "@/containers/FeaturePopup";

export default {
  name: 'TheMap',
  components: {FeaturePopup, TreeView},
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

    console.log('map loaded')
  }
}
</script>
