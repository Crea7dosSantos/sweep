<template>
  <div>
    <p>this is totos list page</p>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  components: {},
  data: function() {
    return {
      // todos: []
      message: ''
    }
  },
  beforeMount: function() {
    let axios = Axios.create({
      baseURL: 'http://localhost:5000',
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      },
      responsetype: 'json'
    })
    // let self = this
    axios
      .get('/')
      .then(res => {
        if (res.status === 200) {
          console.log('success get api')
          console.log(res.data)
          // self.todos = res.data
          // self.message = res.data.message
        }
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
