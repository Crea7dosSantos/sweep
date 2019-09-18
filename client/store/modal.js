export const strict = false

export const state = () => ({
  isUserView: false
})

export const mutations = {
  setUserView(state) {
    state.isUserView = true
  },
  unsetUserView(state) {
    state.isUserView = false
  }
}

export const actions = {
  setUserView({ commit }) {
    commit('setUserView')
  },
  unsetUserView({ commit }) {
    commit('unsetUserView')
  }
}
