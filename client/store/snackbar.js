export const state = () => ({
  message: false,
  status: ''
})

export const mutations = {
  setMessage(state, payload) {
    state.message = payload
  }
}

export const actions = {
  snackOn({ commit }, payload) {
    commit('setMessage', payload)
  },
  snakOff({ commit }) {
    commit('setMessage', false)
  }
}

export const getters = {
  isMessage(state) {
    return !!state.message
  }
}
