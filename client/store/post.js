import Axios from 'axios'
export const strict = false

export const state = () => ({
  posts: []
})

export const mutations = {
  init(state, payload) {
    state.posts = payload
  }
}

export const actions = {
  init({ commit }, token) {
    const axiosAccess = Axios.create({
      baseURL: 'http://localhost:5000',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + token
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
      })
  }
}
