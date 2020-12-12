<template>
  <div id="app">
    <treeselect v-model="$store.state.treeData.values"
                :multiple="true"
                :alwaysOpen="true"
                :options="$store.state.treeData.options"
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
function changeStyleOfSelection(event, style){

  if(event.children) {
    event.children.forEach(child => changeStyleOfSelection(child, style));
    //alert('root clicked');
  }
  else {
  }
}

function extractCsvNames(csvTree, root){
  return csvTree.map((currElement) => {
    const node = Object.entries(currElement)[0];
    return {
      id: uuid.v1(),
      label: node[0],
      children: extractColumnNames(node[1], root, node[0]),
      root: root,
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

        store.state.treeData.options = Object.entries(a.data).map(x => {
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
    '$store.state.treeLevel': function() {
      console.log(this.$store.state.treeLevel)
    }
  },
  methods: {
    onselect: function (event) {
      if(event.columnId != null) {
        //TODO: Térképi diagramm
        alert(event.columnId)
      }
      if(event.csv != null) {
        this.$store.state.correlationUrl = `http://localhost:5000/correlation/${event.root}/${event.csv}`;
      }
      console.log(event)
      //changeStyleOfSelection(event, MarkerService.checkedStyle);
    },
    oninput: function (event) {
      console.log('input changed', event);
    },
    ondeselect: event => {
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
  z-index: 1000;
}

.vue-treeselect__menu{
  width: 1000px!important;
}
</style>
