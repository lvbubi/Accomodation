<template>
  <div ref="popup" class="ol-popup">
    <a href="#" ref="popup-closer" class="ol-popup-closer"></a>
    <div ref="popup-content"></div>
  </div>
</template>

<script>
import {Overlay} from "ol";
import * as axios from "axios";

export default {
  name: "FeaturePopup",
  props: {
    map: {}
  },

  mounted() {
    const container = this.$refs['popup'];
    const content = this.$refs['popup-content'];
    const closer = this.$refs['popup-closer'];

    const overlay = new Overlay({
      element: container,
      autoPan: true,
      autoPanAnimation: {
        duration: 250,
      },
    });

    closer.onclick = function () {
      overlay.setPosition(undefined);
      closer.blur();
      return false;
    };

    this.$nextTick(() => {

      this.map.addOverlay(overlay);
      this.map.on('singleclick', evt => {
        const feature = this.map.forEachFeatureAtPixel(evt.pixel, x => x);
        if(!feature) {
          overlay.setPosition(undefined);
          closer.blur();
          return;
        }

        const path = feature.get('path');
        const id = feature.get('id')

        axios.default.get(`http://localhost:5000/meta/${path}/${id}`).then((a) => {
          const attributes = Object.entries(a.data).map(x => `<br><code>${x[0]}: ${x[1]}</code>`)

          content.innerHTML = `<p>You clicked here: ${a.data.title}</p>` + attributes;
          overlay.setPosition(evt.coordinate);
        });
      });

    })
  }

}
</script>

<style scoped>
  .ol-popup {
    position: absolute;
    background-color: white;
    box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #cccccc;
    bottom: 12px;
    left: -50px;
    min-width: 280px;
  }
  .ol-popup:after, .ol-popup:before {
    top: 100%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  .ol-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
  }
  .ol-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
  }
  .ol-popup-closer {
    text-decoration: none;
    position: absolute;
    top: 2px;
    right: 8px;
  }
  .ol-popup-closer:after {
    content: "✖";
  }
</style>
