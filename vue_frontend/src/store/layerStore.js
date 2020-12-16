import Vue from "vue";
import Vuex from "vuex";
import MarkerService from "@/containers/MarkerService";

Vue.use(Vuex);

function searchTree(element, matchingTitle){
    if(element.id === matchingTitle){
        return element;
    }else if (element.children != null){
        var i;
        var result = null;
        for(i=0; result == null && i < element.children.length; i++){
            result = searchTree(element.children[i], matchingTitle);
        }
        return result;
    }
    return null;
}


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

const getters = {
    selectVisible: state => {
        if(!state.treeData.values || state.treeData.values.length === 0){
            return false;
        }

        const selectedElement = searchTree({
            children : state.treeData.options
        }, "" + state.treeData.values)

        return selectedElement.label.endsWith('.csv');

    }
}

export default {
    state,
    mutations,
    getters
}
