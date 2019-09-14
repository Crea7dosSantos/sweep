import Axios from 'axios'
import Cookies from 'js-cookie'

const accessToken = Cookies.get('access_token')

const axiosAccess = Axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer ' + accessToken
  },
  responseType: 'json'
})

export default axiosAccess
