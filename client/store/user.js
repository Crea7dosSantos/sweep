import Axios from 'axios'
export const strict = false

const initialState = {
  name: '',
  id: '',
  email: '',
  profileImageKey: null,
  backImageKey: null
}

export const state = () => ({
  user: initialState,
  loggedIn: false
})

export const mutations = {
  setUserState(state, payload) {
    const userObj = payload[0]
    state.user.name = userObj.username
    state.user.id = userObj.id
    state.user.email = userObj.email
    state.user.profileImageKey = userObj.profile_image_key
    state.user.backImageKey = userObj.profile_back_image_key
    state.loggedIn = true
  },
  unsetUserState(state) {
    state.user.name = ''
    state.user.id = ''
    state.user.email = ''
    state.user.profileImageKey = null
    state.user.backImageKey = null
    state.loggedIn = false
  }
}

export const actions = {
  setUserState({ commit }, token) {
    const axiosAccess = Axios.create({
      baseURL: 'http://localhost:5000',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + token
      },
      responseType: 'json'
    })
    axiosAccess
      .get('/protected')
      .then(res => {
        const data = res.data
        const payload = data.user_datas
        commit('setUserState', payload)
      })
      .catch(() => {
        commit('setUserStete', false)
      })
  },
  unsetUserState({ commit }) {
    commit('unsetUserState')
  }
}

export const getters = {
  isAuthenticated(state) {
    return !!state.loggedIn
  },
  isAuthProfileImage(state) {
    return !!state.user.profileImageKey
  },
  isAuthBackImage(state) {
    return !!state.user.backImageKey
  }
}
