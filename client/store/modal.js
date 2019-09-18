export const strict = false

export const state = () => ({
  isUserView: false,
  isSigninView: false,
  isSignupView: false,
  isSignoutView: false
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
  setSignunView({ commit }) {
    commit('setSignunView')
  },
  unsetSignunView({ commit }) {
    commit('unsetSignunView')
  },
  setSignoutView({ commit }) {
    commit('setSignoutView')
  },
  unsetSignoutView({ commit }) {
    commit('unsetSignoutView')
  }
}
