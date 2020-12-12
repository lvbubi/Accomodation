<template>
  <div></div>
</template>
<script>
import marker_default from "./../assets/icons/marker.png";
import marker_selected from "./../assets/icons/marker_selected.png";
import { Vector } from 'ol/layer';
import { Vector as VectorSource } from 'ol/source';
import { Icon, Style } from 'ol/style';
import Stroke from "ol/style/Stroke";
import Fill from "ol/style/Fill";

const checkedStyle = new Style({
  image: new Icon({
    anchor: [0.5, 46],
    anchorXUnits: 'fraction',
    anchorYUnits: 'pixels',
    src: marker_selected
  })
});

const defaultStyle = new Style({
  image: new Icon({
    anchor: [0.5, 46],
    anchorXUnits: 'fraction',
    anchorYUnits: 'pixels',
    src: marker_default
  })
});

export default {
  name: 'MarkerService',
  checkedStyle,
  defaultStyle,
  markerVector: () => {
    return new Vector({
      name: 'markers',
      source: new VectorSource({
        features: []
      }),
      maxZoom: 18,
      minZoom: 2,
      style: defaultStyle
    })
  },
  baszottVector: () => {
    return new Vector({
      name: 'markers',
      source: new VectorSource({
        features: []
      }),
      maxZoom: 18,
      minZoom: 2,
      style: new Style({
        stroke: new Stroke({
          color: 'blue',
          width: 3
        }),
        fill: new Fill({
          color: 'rgba(0, 0, 255, 0.1)'
        })
      })
    })
  }
}
</script>
