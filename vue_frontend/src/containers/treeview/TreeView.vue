<template>
  <div id="app">
    <treeselect v-model="$store.state.LayerStore.treeData.values"
                :multiple="false"
                :alwaysOpen="true"
                :options="$store.state.LayerStore.treeData.options"
                @select="onselect"
                @input="oninput"
                @deselect="ondeselect"
    />
  </div>
</template>

<script>
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
import * as axios from "axios";
import { uuid } from 'vue-uuid';
import LayerStore from '@/store/layerStore';
import {createFeature} from "@/containers/treeview/FeatureService";

function extractCsvNames(csvTree, root){
  return csvTree.map((currElement) => {
    const node = Object.entries(currElement)[0];
    return {
      id: uuid.v1(),
      label: node[0],
      children: extractColumnNames(node[1], root, node[0]),
      root: root,
      path: `${root}/${node[0]}`,
      csv: node[0]
    }
  });
}

function extractColumnNames(columnNames, root, parent){
  const ids = Object.entries(columnNames.id);
  const titles = Object.entries(columnNames.title);

  return ids.map((node, index) => {
    return {
      id: uuid.v1(),
      label: titles[index][1],
      root: root,
      csv: parent,
      path: `${root}/${parent}/${node[1]}`,
      columnId: node[1]
    }
  });
}

export default {
  name: 'TheTreeView',
  // register the component
  components: { Treeselect },
  props: {
    map: {},
  },
  mounted() {
    this.$nextTick(() => {
      const map = this.map;
      const store = this.$store;

      map.on('moveend', e => {
        let newZoom = map.getView().getZoom();
        if (store.state.zoomLevel !== newZoom) {
          store.commit("changeZoomLevel", newZoom);
        }
      });

      //axios.default.get('http://localhost:5000/' + this.$store.state.treeLevel).then((a) => {
      axios.default.get('http://localhost:5000/tree').then((a) => {
        console.log(a.data);

        LayerStore.state.treeData.options = Object.entries(a.data).map(x => {
          return {
            id: x[0],
            label: x[0],
            children: extractCsvNames(x[1], x[0])
          }
        });
      });
    });
  },
  watch: {
    '$LayerStore.state.treeLevel': function() {
      console.log(this.LayerStore.state.treeLevel)
    }
  },
  methods: {
    onselect: function (event) {
      LayerStore.state.circleLayer.getSource().clear();

      const chartType = event.columnId != null ? "scatter" : this.$store.state.chartType;

      const path = [event.root, event.csv, event.columnId].filter(x => x != null).join('/')

      if(event.csv != null) {
        this.$store.state.chartUrl = `http://localhost:5000/${chartType}/${path}`;
      }

      if(event.columnId != null) {
        //event.root a zoomlevelhez legyen kötődve

        axios.default.get(`http://localhost:5000/percentage/${path}`).then((a) => {
          const features = a.data.map(x => createFeature(x, path))
          LayerStore.state.circleLayer.getSource().addFeatures(features);
        });
      }
    },
    oninput: function (event) {
      console.log('input changed', event);
    },
    ondeselect: event => {
      LayerStore.state.circleLayer.getSource().clear();
      //changeStyleOfSelection(event, MarkerService.defaultStyle);
    }
  }
}
</script>

<!-- Using the `scoped` attribute -->
<style scoped>
.vue-treeselect {
  width: 30%;
  position: absolute;
  right: 0;
  z-index: 100;
}

.vue-treeselect__menu{
  width: 1000px!important;
}
</style>
