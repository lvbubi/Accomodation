<template>
  <CSidebar
      fixed
      :minimize="minimize"
      :show="show"
      :overlaid="!minimize"

      @update:show="(value) => $store.commit('set', ['sidebarShow', value])"
  >
    <CSidebarBrand class="d-md-down-none" to="/">
      <v-img contain src="http://oktatas.mik.uni-pannon.hu/pluginfile.php/1/theme_enlightlite/logo/1604907398/cimer_szines_99_transparent.png" max-height="150px"></v-img>
    </CSidebarBrand>

    <CSelect
        label="Correlation Type"
        :options="['correlation/pearson', 'correlation/spearman', 'correlation/kendall']"
        @update:value="(value) => $store.state.chartType = value"
        :value="$store.state.chartType"
        v-if="$store.getters.selectVisible"
        style="padding-left: 10px; padding-right: 30%;"
    />
    <img :src="$store.state.chartUrl" class="square" @click="$modal.show('size-modal')">

    <CSidebarMinimizer
        class="d-md-down-none"
        style="bottom: 0; position: absolute"
        @click.native="$store.commit('set', ['sidebarMinimize', !minimize])"
    />
  </CSidebar>
</template>

<script>
import nav from './_nav'
import DoughnutChart from "@/containers/DoughnutChart";

export default {
  name: 'TheSidebar',
  nav,
  components: {
    DoughnutChart
  },
  data: () => {
    return {
      dropdown: [      {
        _name: 'CSidebarNavItem',
        name: 'Charts',
        to: '/charts',
        icon: 'cil-chart-pie'
      }]
    }
  },
  computed: {
    show() {
      return this.$store.state.sidebarShow
    },
    minimize() {
      return this.$store.state.sidebarMinimize
    }
  },
  watch: {
    '$store.state.chartType': function(state, oldValue) {
      this.$store.state.chartUrl = this.$store.state.chartUrl.replace(oldValue, state);
    }
  }
}
</script>

<style scoped>
  .visible{
    opacity: 1;
  }
  .invisible{
    opacity: 0;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }

  .square {
    width: 100%;
  }

  .square:after {
    content: "";
    display: block;
  }
</style>
