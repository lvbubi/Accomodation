import MarkerService from "@/containers/MarkerService";

function searchTree(element, matchingTitle){
    if(element.id === matchingTitle){
        return element;
    }else if (element.children != null){
        let i;
        let result = null;
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

const selectedNode = state => {
    return  searchTree({
        children : state.treeData.options
    }, "" + state.treeData.values)
}

const getters = {
    selectVisible: state => {
        if(!state.treeData.values || state.treeData.values.length === 0){
            return false;
        }

        return selectedNode(state).label.endsWith('.csv');
    },
    selectedNode
}

export default {
    state,
    mutations,
    getters
}
