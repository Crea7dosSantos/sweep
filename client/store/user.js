import Axios from 'axios'
export const strict = false

const initialState = {
  name: '',
  id: '',
  email: ''
}

export const state = () => ({
  user: initialState
})

export const mutations = {
  setUserState(state, payload) {
    const userObj = payload[0]
    state.user.name = userObj.username
    state.user.id = userObj.id
    state.user.email = userObj.email
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
        console.log(data.user_datas)
        const payload = data.user_datas
        commit('setUserState', payload)
      })
      .catch(() => {
        commit('setUserStete', false)
      })
  },
  signOut({ commit }) {
    commit('setUserstate', false)
  }
}

export const getters = {
  isAuthenticated(state) {
    return !!state.user
  }
}
