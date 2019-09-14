import Axios from 'axios'
import Cookies from 'js-cookie'

const axiosAccess = Axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer ' + Cookies.get('access_token')
  },
  responseType: 'json'
})

export default axiosAccess
