export const strict = false

export const state = () => ({
  isUserView: false
})

export const mutations = {
  setUserView(state, payload) {
    state.isUserView = payload
  }
}

export const actions = {
  setUserView({ commit }, payload) {
    commit('setUserView', payload)
  }
}
