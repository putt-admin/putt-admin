import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000,
});

class APIs {
  login(username, password) {
    return instance.post(`/token/`, {
      username,
      password,
    })
  }
}

const API = new APIs()
export default API
