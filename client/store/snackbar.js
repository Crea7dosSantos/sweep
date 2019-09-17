export const strict = false

export const state = () => ({
  isEnable: false,
  message: false,
  status: ''
})

export const mutations = {
  setMessage(state, payload) {
    state.isEnable = true
    state.message = payload
  },
  setDisable(state) {
    state.isEnable = false
  }
}

export const actions = {
  snackOn({ commit }, payload) {
    commit('setMessage', payload)
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
