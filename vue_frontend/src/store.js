import Vue from 'vue';
import Vuex from 'vuex';
import layerStore from "@/store/layerStore";

Vue.use(Vuex);

const state = {
  sidebarShow: 'responsive',
  sidebarMinimize: false,
  zoomLevel: 0,
  chartType: 'correlation',
  chartUrl: 'https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-law.gif',
}

const mutations = {
  changeZoomLevel (state, newZoomLevel) {
    if(state.zoomLevel > 10){
      if(newZoomLevel <= 10){
        console.log('CHANGE TREE TO COUNTY LEVEL');
        state.LayerStore.treeLevel = 'county';
      }
    }
    else{
      if(newZoomLevel > 10){
        console.log('CHANGE TREE TO TOWN LEVEL');
        state.LayerStore.treeLevel = 'town';
      }
    }
    state.zoomLevel = newZoomLevel;
  },

  toggleSidebarDesktop (state) {
    const sidebarOpened = [true, 'responsive'].includes(state.sidebarShow)
    state.sidebarShow = sidebarOpened ? false : 'responsive'
  },
  toggleSidebarMobile (state) {
    const sidebarClosed = [false, 'responsive'].includes(state.sidebarShow)
    state.sidebarShow = sidebarClosed ? true : 'responsive'
  },
  set (state, [variable, value]) {
    state[variable] = value
  }
}

export default new Vuex.Store({
  modules: {
    LayerStore: layerStore
  },
  state,
  mutations
})
