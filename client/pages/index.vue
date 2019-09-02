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
                    class="input is-medium"
                    type="text"
                    placeholder="Todo name input"
                    v-model="todoName"
                  />
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button is-dark" @click="create">Create Todo</button>
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
                <td class="has-text-weight-semibold td-font">{{ todo["date_posted"] }}</td>
                <td>
                  <button class="button is-primary">Primary</button>
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
import Axios from 'axios'

export default {
  components: {},
  data: function() {
    return {
      todos: [],
      todoName: ''
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
    let self = this
    axios
      .get('/')
      .then(res => {
        if (res.status === 200) {
          console.log('success get api')
          console.log(res.data)
          self.todos = res.data.todos
        }
      })
      .catch(error => {
        console.log(error)
      })
  },
  methods: {
    create: function() {
      const max = 255
      const min = 5
      if (
        !this.todoName == '' &&
        this.todoName.length > min &&
        this.todoName.length < max
      ) {
        console.log('add todo successs')
      } else {
        console.log('errorやで')
      }
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
