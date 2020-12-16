<template>
  <modal
      name="size-modal"
      classes="demo-modal-class"
      :min-width="200"
      :min-height="200"
      :scrollable="true"
      :reset="true"
      width="60%"
      height="auto"
      @before-open="beforeOpen"
      @opened="opened"
      @before-close="beforeClose"
      @closed="closed"
  >
    <div class="size-modal-content">
      <div class="grid-container">
        <div class="item3">
          <img :src="image"/>
        </div>
        <div class="item4 center" v-html="metaData">Right</div>
      </div>
    </div>
  </modal>
</template>
<script>
import * as axios from "axios";

export default {
  name: 'ModalAutosize',
  data() {
    return {
      image: {},
      metaData: 'cica'
    }
  },
  methods: {
    beforeOpen(event) {
      this.image = this.$store.state.chartUrl;

      const path = this.$store.getters.selectedNode.path

      axios.default.get(`http://localhost:5000/chart/meta/${path}`).then((a) => {
        console.log(a);
        console.log(Array.isArray(a.data));
        if(Array.isArray(a.data)){
          this.metaData = a.data.map(x => `<p>${x}</p>`).join('\n');
        }
        else{
          this.metaData = Object.entries(a.data).map(x => `<p>${x[0]}: ${x[1]}</p>`).join('\n');
        }
      });

      console.log('before-open', event)
    },
    beforeClose() {
      clearInterval(this.timer)
      this.timer = null
    },
    opened(event) {
      console.log('opened', event)
    },
    closed(event) {
      console.log('closed', event)
    }
  }
}
</script>
<style>
.size-modal-content {
  padding: 10px;
  font-style: 13;
}

.v--modal-overlay[data-modal='size-modal'] {
  background: rgba(0, 0, 0, 0.5);
}

.demo-modal-class {
  border-radius: 5px;
  background: #f7f7f7;
  box-shadow: 5px 5px 30px 0px rgba(46, 61, 73, 0.6);
}

.break-word {
  display: inline-block;
  word-wrap: break-word;
}

.item3 { grid-area: main; }
.item4 { grid-area: right; }

.grid-container {
  display: grid;
  grid-template-areas:
    'main right';
  padding: 10px;
}

.grid-container > div {
  text-align: center;
  padding: 0px 0;
  font-size: 14px;
}

.center {
  margin: auto;
}
</style>
