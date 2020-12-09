<template>
  <CChartDoughnut
      :datasets="defaultDatasets"
      :options="options"
      :labels="labels"
  />
</template>

<script>
import { CChartDoughnut } from '@coreui/vue-chartjs';
import json from './chart-colors.json';

export default {
  name: 'DoughnutChart',
  components: { CChartDoughnut },

  data: () => ({
    options: {
      legend: {
        display: false,
        position: 'bottom'
      }
    },
    colors: []
  }),
  mounted() {
    console.log('char created');
    console.log(this.colors);
  },
  created() {
    console.log('char created');
    this.colors = json;
  },
  computed: {
    defaultDatasets () {
      const numberOfPackages = 2
      return [
        {
          backgroundColor: this.colors.slice(0, numberOfPackages),
          data: [10,20]
        }
      ]
    },
    labels() {
      return [1,2]
    }
  }
}
</script>
