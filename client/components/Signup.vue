<template>
  <v-dialog v-model="userSignupVisible" width="450px">
    <v-card class="elevation-12">
      <v-toolbar flat>
        <v-toolbar-title class="grey--text">Sign up</v-toolbar-title>
        <div class="flex-grow-1" />
      </v-toolbar>
      <v-divider class="mb-4" />
      <v-card-text class="pb-0">
        <v-form ref="form">
          <v-text-field
            v-model="userName"
            label="Username"
            :rules="[rules.required, rules.min4]"
            name="Username"
            prepend-icon="person"
            type="text"
            counter
            maxlength="20"
            required
          />
          <v-text-field
            v-model="email"
            label="Email"
            :rules="[rules.required, rules.email]"
            name="Email"
            prepend-icon="email"
            type="email"
            required
          />
          <v-text-field
            id="password"
            v-model="password"
            :rules="[rules.required, rules.min4, rules.max20]"
            label="Password"
            name="password"
            prepend-icon="lock"
            type="password"
            required
          />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn class="me-4 mb-3" color="primary" @click="signup">Sign up</v-btn>
      </v-card-actions>
      <div class="signin-div">
        <p class="subtitle-1 mb-0">
          Already a member?
          <v-btn @click="displaySigninView" text small color="primary">Sign in</v-btn>
        </p>
      </div>
    </v-card>
  </v-dialog>
</template>

<script>
import axiosBase from '@/plugins/axiosBase'
import { mapState, mapActions } from 'vuex'

export default {
  props: {},
  data: () => ({
    drawer: null,
    userName: '',
    email: '',
    password: '',
    rules: {
      required: value => !!value || 'Required.',
      min4: value => value.length >= 4 || 'Min 4 characters',
      max20: value => value.length <= 20 || 'Max 20 characters',
      email: value => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || 'Invalid e-mail.'
      }
    }
  }),
  computed: {
    ...mapState('modal', ['isSignupView']),
    userSignupVisible: {
      get() {
        return this.isSignupView
      },
      set() {
        return this.$store.dispatch('modal/unsetSignupView')
      }
    }
  },
  methods: {
    ...mapActions('snackbar', ['snackOn']),
    ...mapActions('modal', ['unsetSignupView']),
    ...mapActions('modal', ['setSigninView']),
    signup: function() {
      if (!this.$refs.form.validate()) {
        return
      }
      let self = this
      axiosBase
        .post('/signup', {
          username: self.userName,
          email: self.email,
          password: self.password
        })
        .then(res => {
          this.snackOn({ payload: 'Success create account', color: 'green' })
          console.log(res.data.message)
          this.unsetSignupView()
          this.setSigninView()
        })
        .catch(error => {
          console.log(error)
          this.snackOn({ payload: 'Error create account' })
        })
    },
    displaySigninView: function() {
      this.unsetSignupView()
      this.setSigninView()
    }
  }
}
</script>

<style scoped>
.v-divider {
  margin: 0px;
}
.signin-div {
  padding-bottom: 10px;
}
</style>
