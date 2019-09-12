import Axios from 'axios'
export const strict = false

export const state = () => ({
  user: false
})

export const mutations = {
  setUserState(state, payload) {
    state.user = payload
  }
}

export const actions = {
  signIn({ commit }, token) {
    let axios = Axios.create({
      baseURL: 'http://localhost:5000',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + token
      },
      responseType: 'json'
    })
    axios
      .get('/protected')
      .then(res => {
        const data = res.data
        console.log(data)
        const payload = data.user_name
        commit('setUserState', payload)
      })
      .catch(() => {
        commit('setUserStete', false)
      })
  },
  signout({ commit }) {
    commit('setUserstate', false)
  }
}

export const getters = {
  isAuthenticated(state) {
    return !!state.user
  }
}
