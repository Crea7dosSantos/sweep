<template>
  <div class="container-block">
    <section class="hero is-primary is-bold">
      <div class="hero-body">
        <div class="container new-todo">
          <h3 class="title is-3">New Todo</h3>
          <div class="columns">
            <div class="column is-four-fifths">
              <div class="field">
                <label class="label has-text-white">Name</label>
                <div class="control">
                  <input
                    v-model="todoName"
                    class="input is-medium"
                    :class="{ 'input is-danger': isErrorExist }"
                    type="text"
                    placeholder="Todo name input"
                  />
                  <p class="help is-danger">{{ error }}</p>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button
                    class="button is-dark"
                    :class="{ 'is-loading': isLoading }"
                    @click="create"
                  >Create Todo</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <div class="container todo-list">
      <h3 class="title is-3">Todo List</h3>
      <div class="columns">
        <div class="column is-full">
          <table class="table is-fullwidth is-hoverable">
            <thead>
              <tr>
                <th>title</th>
                <th>date_posted</th>
                <th />
              </tr>
            </thead>
            <tbody>
              <tr v-for="(todo, index) in todos" :key="index">
                <td class="has-text-weight-semibold td-font">{{ todo["title"] }}</td>
                <td class="has-text-weight-semibold td-font">{{ todo["date_posted"] | dateFormat }}</td>
                <td>
                  <button class="button is-primary" @click="deleteHandler(todo.id)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosBase from '@/plugins/axiosBase'
import Axios from 'axios'
import Cookies from 'js-cookie'
import { mapActions } from 'vuex'

export default {
  components: {},
  data: function() {
    return {
      todos: [],
      todoName: '',
      error: '',
      isErrorExist: false,
      isLoading: false,
      token: ''
    }
  },
  watch: {
    todoName: function(newVal) {
      newVal.length <= 4 && !newVal.length == 0
        ? ((this.error = 'character length error'), (this.isErrorExist = true))
        : ((this.error = ''), (this.isErrorExist = false))
    }
  },
  mounted: function() {
    const router = this.$router
    let self = this
    let token = Cookies.get('access_token')
    if (!token) {
      this.snackOn('Please sign in')
      return
    }
    this.axiosAccessHandler(Cookies.get('access_token'))
      .get('/home')
      .then(res => {
        self.todos = res.data.todos
      })
      .catch(() => {
        console.log('error is /home')
        this.axiosRefreshHandler(Cookies.get('refresh_token'))
          .post('/refresh')
          .then(res => {
            console.log('get new access_token')
            Cookies.set('access_token', res.data.access_token)
            location.reload()
          })
          .catch(() => {
            this.snackOn('Please sign in again')
            this.signOut()
            Cookies.remove('access_token')
            Cookies.remove('refresh_token')
            router.push('/signin')
          })
      })
  },
  methods: {
    ...mapActions('snackbar', ['snackOn']),
    create: function() {
      const self = this
      self.isLoading = true
      if (this.todoName == '') {
        this.error = 'This item is not allowed to be empty'
        console.log('not create todo')
        self.isLoading = false
        return
      } else if (this.isErrorExist == true) {
        self.isLoading = false
        return
      }
      console.log('add todo create success')
      this.axiosAccessHandler(Cookies.get('access_token'))
        .post('/create', { title: self.todoName })
        .then(res => {
          if (res.status === 200) {
            console.log('success post todo')
            self.isLoading = false
            self.todoName = ''
            self.isErrorExist = false
            this.snackOn('Created a new Todo')
            this.axiosAccessHandler(Cookies.get('access_token'))
              .get('/home')
              .then(res => {
                if (res.status === 200) {
                  console.log('success get api')
                  self.todos = res.data.todos
                }
              })
              .catch(error => {
                console.log(error)
              })
          }
        })
        .catch(error => {
          console.log(error)
          self.isLoading = false
        })
    },
    deleteHandler: function(todoId) {
      console.log(todoId)
      axiosBase
        .post('/delete', { delete_id: todoId })
        .then(res => {
          if (res.status === 200) {
            this.snackOn('Deleted a new Todo')
          }
        })
        .catch(error => {
          console.log(error)
          self.isLoading = false
        })
    },
    axiosAccessHandler: function(token) {
      const axiosAccess = Axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + token
        },
        responseType: 'json'
      })
      return axiosAccess
    },
    axiosRefreshHandler: function(token) {
      const axiosRefresh = Axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + token
        },
        responseType: 'json'
      })
      return axiosRefresh
    }
  }
}
</script>

<style>
.todo-list {
  margin-top: 50px;
}
.td-font {
  color: gray;
  font-size: 17px;
}
.table td {
  vertical-align: middle;
}
.new-todo {
  margin-top: 20px;
}
</style>
