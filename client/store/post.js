import Axios from 'axios'
import Cookies from 'js-cookie'
export const strict = false

export const state = () => ({
  posts: []
})

export const mutations = {
  init(state, payload) {
    state.posts = payload
  },
  unset(state) {
    state.posts = []
  }
}

export const actions = {
  init({ commit }, accessToken, refreshToken) {
    const axiosAccess = Axios.create({
      baseURL: 'http://localhost:5000',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + accessToken
      },
      responseType: 'json'
    })
    axiosAccess
      .get('/home')
      .then(res => {
        const data = res.data.todos
        commit('init', data)
      })
      .catch(() => {
        console.log('Failed to get data')
        const axiosRefresh = Axios.create({
          baseURL: 'http://localhost:5000',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + refreshToken
          },
          responseType: 'json'
        })
        axiosRefresh
          .post('/refresh')
          .then(res => {
            Cookies.set('access_token', res.data.access_token)
            location.reload()
          })
          .catch(() => {
            Cookies.remove('access_token')
            Cookies.remove('refresh_token')
            location.reload()
          })
      })
  },
  unset({ commit }) {
    commit('unset')
  }
}
