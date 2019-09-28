<template>
  <div class="container">
    <!-- <section class="hero is-primary is-bold">
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
    </section>-->

    <!-- <section class="create-part">
      <div class="hero-body">
        <div class="container new-todo">
          <h3 class="title is-3">Post</h3>
          <div class="columns">
            <div class="column is-four-fifths">
              <v-text-field
                label="your post title"
                v-model="todoName"
                :class="{ 'input is-danger': isErrorExist }"
                placeholder="Post title"
              ></v-text-field>
              <p class="help is-danger">{{ error }}</p>
              <v-textarea></v-textarea>
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
    </section>-->
    <!-- <div class="container todo-list">
    <h3 class="title is-3">All Post</h3>-->
    <!-- <div class="columns">
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
    <div>-->
    <v-app>
      <h3 class="title is-3">
        All Post
      </h3>
      <div>
        <v-col
          v-for="(todo, index) in todos"
          :key="index"
        >
          <v-card
            max-width="400"
            class="mx-auto"
          >
            <v-img
              :src="'https://' + bucketName + baseURL + todo.post_image_key"
              class="white--text"
              height="200px"
            >
              <!-- "https://sweep-user-back-image.s3.amazonaws.com/sunset-2137067_1920%20(1).jpg" -->

              <v-card-title
                class="align-end fill-height"
                max-width="400"
              >
                {{ todo["title"] }}
              </v-card-title>
            </v-img>
            <v-card-text>
              <span>{{ todo["date_posted"] | dateFormat }}</span>
              <br>
              <span class="text--primary">
                <span>{{ todo.content }}</span>
                <br>
              </span>
            </v-card-text>
            <!-- <td class="has-text-weight-semibold td-font">{{ todo["date_posted"] | dateFormat }}</td>
            <td>
              <button class="button is-primary" @click="deleteHandler(todo.id)">Delete</button>
            </td>-->
          </v-card>
        </v-col>
      </div>
      <template>
        <AllModal />
        <User />
      </template>
    </v-app>
  </div>
</template>

<script>
import Axios from 'axios'
import Cookies from 'js-cookie'
import { mapActions } from 'vuex'
import AllModal from '~/components/AllModal'
import User from '~/components/User'

export default {
  components: {
    AllModal,
    User
  },
  data: function() {
    return {
      todos: [],
      todoName: '',
      content: '',
      error: '',
      isErrorExist: false,
      isLoading: false,
      token: '',
      bucketName: process.env.POST_IMAGE_BUCKET_NAME,
      baseURL: process.env.BASE_URL
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
    let token = this.getToken()
    if (!token) {
      this.snackOn({ payload: 'Please sign in', color: 'error' })
      return
    }
    this.axiosAccessHandler()
      .get('/home')
      .then(res => {
        self.todos = res.data.todos
      })
      .catch(() => {
        this.snackOn({ payload: 'Rebuilding page', color: 'blue' })
        this.axiosRefreshHandler()
          .post('/refresh')
          .then(res => {
            console.log('get new access_token')
            Cookies.set('access_token', res.data.access_token)
            location.reload()
          })
          .catch(() => {
            this.snackOn({ payload: 'Please sign in again', color: 'yellow' })
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
        self.isLoading = false
        return
      } else if (this.isErrorExist == true) {
        self.isLoading = false
        return
      }
      this.axiosAccessHandler()
        .post('/create', { title: self.todoName })
        .then(() => {
          self.isLoading = false
          self.todoName = ''
          self.isErrorExist = false
          this.snackOn({ payload: 'Created a new Todo', color: 'green' })
        })
        .catch(() => {
          this.snackOn({ payload: 'Can not create Todo', color: 'error' })
          self.isLoading = false
          return
        })
      this.getTodo(self)
    },
    deleteHandler: function(todoId) {
      const self = this
      this.axiosAccessHandler()
        .post('/delete', { delete_id: todoId })
        .then(() => {
          this.snackOn({ payload: 'Deleted a new Todo', color: 'green' })
        })
        .catch(() => {
          this.snackOn({ payload: 'Not deleted a new Todo', color: 'error' })
          self.isLoading = false
          return
        })
      this.getTodo(self)
    },
    axiosAccessHandler: function() {
      const axiosAccess = Axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + this.getToken()
        },
        responseType: 'json'
      })
      return axiosAccess
    },
    axiosRefreshHandler: function() {
      const axiosRefresh = Axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + this.getToken()
        },
        responseType: 'json'
      })
      return axiosRefresh
    },
    getTodo: function(self) {
      this.axiosAccessHandler()
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
    },
    getToken: function() {
      return Cookies.get('access_token')
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
.create-part {
  background: lightgray;
}
.container {
  margin-top: 20px;
}
</style>
