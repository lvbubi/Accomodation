<template>
  <div class="c-app">
    <ModalAutosize></ModalAutosize>
    <TheSidebar/>
    <CWrapper>
      <div class="c-body">
        <main class="c-main" style="padding: 0px">
          <TheMap/>
        </main>
      </div>
    </CWrapper>
  </div>
</template>

<script>
import TheSidebar from './TheSidebar'
import TheMap from './TheMap'
import ModalAutosize from "@/containers/ModalAutosize";

export default {
  name: 'TheContainer',
  components: {
    ModalAutosize,
    TheSidebar,
    TheMap
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
