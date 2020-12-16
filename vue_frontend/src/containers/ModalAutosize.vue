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
      <div>
        A new paragraph will be added every 5 sec to show how
        <b>height</b> scales.
      </div>
      <div class="row">
        <div class="column">
          <img :src="image"/>
        </div>
        <div class="column">
          cica
        </div>
      </div>
    </div>
  </modal>
</template>
<script>
export default {
  name: 'ModalAutosize',
  data() {
    return {
      image: {}
    }
  },
  methods: {
    beforeOpen(event) {
      this.image = this.$store.state.chartUrl;
      console.log('before-open', event)
    },
    beforeClose() {
      clearInterval(this.timer)
      this.timer = null
    },
    opened(event) {
      this.timer = setInterval(() => {
        this.paragraphs.push(null)
      }, 5000)
      // e.ref should not be undefined here
      console.log('opened', event)
      console.log('ref', event.ref)
      console.log(this.$store.getters.selectedNode)
    },
    closed(event) {
      this.paragraphs = []
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
</style>
