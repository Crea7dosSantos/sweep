import Axios from 'axios'
import Cookies from 'js-cookie'

const refreshToken = Cookies.get('refresh_token')

const axiosRefresh = Axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer ' + refreshToken
  },
  responseType: 'json'
})

export default axiosRefresh
