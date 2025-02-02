import 'core-js/stable'
import Vue from 'vue'
import App from './App'
import router from './router'
import CoreuiVue from '@coreui/vue'
import { iconsSet as icons } from './assets/icons/icons.js'
import store from './store'
import Toasted from 'vue-toasted';

import VModal from 'vue-js-modal'
import 'nx-card/dist/nx-card.css'
import NxCard from 'nx-card/dist/nx-card.common'

Vue.use(NxCard)



Vue.use(VModal)
Vue.config.performance = true
Vue.use(CoreuiVue)
Vue.use(Toasted)
Vue.prototype.$log = console.log.bind(console)

const VueUploadComponent = require('vue-upload-component')
Vue.component('file-upload', VueUploadComponent)

if (module.hot) {
  module.hot.accept() // already had this init code

  module.hot.addStatusHandler(status => {
    if (status === 'prepare') console.clear()
  })
}

new Vue({
  el: '#app',
  router,
  store,
  icons,
  template: '<App/>',
  components: {
    App
  }
})
