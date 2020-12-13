import Vue from "vue";
import Vuex from "vuex";
import MarkerService from "@/containers/MarkerService";

Vue.use(Vuex);

const state = {
    treeData: {
        options: [],
        values: []
    },
    circleLayer: MarkerService.baszottVector()
}

const mutations = {
    set (state, [variable, value]) {
        state[variable] = value
    }
}

export default new Vuex.Store({
    state,
    mutations
})
