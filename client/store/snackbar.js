export const strict = false

export const state = () => ({
  isEnable: false,
  message: false,
  actionStatus: ''
})

export const mutations = {
  setMessage(state, { payload, color }) {
    state.isEnable = true
    state.message = payload
    state.actionStatus = color
  },
  setDisable(state) {
    state.isEnable = false
  }
}

export const actions = {
  snackOn({ commit }, { payload, color }) {
    commit('setMessage', { payload: payload, color: color })
  },
  snackOff({ commit }) {
    commit('setDisable')
  }
}

export const getters = {
  getEnable(state) {
    return state.isEnable
  }
}
