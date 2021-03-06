export const strict = false

export const state = () => ({
  isUserView: false,
  isSigninView: false,
  isSignupView: false,
  isSignoutView: false,
  isPostView: false
})

export const mutations = {
  setUserView(state) {
    state.isUserView = true
  },
  unsetUserView(state) {
    state.isUserView = false
  },
  setSigninView(state) {
    state.isSigninView = true
  },
  unsetSigninView(state) {
    state.isSigninView = false
  },
  setSignupView(state) {
    state.isSignupView = true
  },
  unsetSignupView(state) {
    state.isSignupView = false
  },
  setSignoutView(state) {
    state.isSignoutView = true
  },
  unsetSignoutView(state) {
    state.isSignoutView = false
  },
  setPostView(state) {
    state.isPostView = true
  },
  unsetPostView(state) {
    state.isPostView = false
  }
}

export const actions = {
  setUserView({ commit }) {
    commit('setUserView')
  },
  unsetUserView({ commit }) {
    commit('unsetUserView')
  },
  setSigninView({ commit }) {
    commit('setSigninView')
  },
  unsetSigninView({ commit }) {
    commit('unsetSigninView')
  },
  setSignupView({ commit }) {
    commit('setSignupView')
  },
  unsetSignupView({ commit }) {
    commit('unsetSignupView')
  },
  setSignoutView({ commit }) {
    commit('setSignoutView')
  },
  unsetSignoutView({ commit }) {
    commit('unsetSignoutView')
  },
  setPostView({ commit }) {
    commit('setPostView')
  },
  unsetPostView({ commit }) {
    commit('unsetPostView')
  }
}
