import Axios from 'axios'
import Cookies from 'js-cookie'

const axiosRefresh = Axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer ' + Cookies.get('refresh_token')
  },
  responseType: 'json'
})

export default axiosRefresh
