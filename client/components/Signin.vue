<template>
  <v-dialog
    v-model="userSigninVisible"
    width="400px"
  >
    <v-card class="elevation-12">
      <v-toolbar flat>
        <v-toolbar-title class="grey--text">
          Sign in
        </v-toolbar-title>
        <div class="flex-grow-1" />
      </v-toolbar>
      <v-divider />
      <v-card-text>
        <v-form ref="form">
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
        <v-btn
          color="primary"
          @click="signin"
        >
          Sign in
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axiosBase from '@/plugins/axiosBase'
import Cookies from 'js-cookie'
import { mapState, mapActions } from 'vuex'

export default {
  props: {},
  data: () => ({
    drawer: null,
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
    ...mapState('modal', ['isSigninView']),
    userSigninVisible: {
      get() {
        return this.isSigninView
      },
      set() {
        return this.$store.dispatch('modal/unsetSigninView')
      }
    }
  },
  methods: {
    ...mapActions('user', ['setUserState']),
    ...mapActions('snackbar', ['snackOn']),
    ...mapActions('modal', ['unsetSigninView']),
    signin: function() {
      const router = this.$router

      if (!this.$refs.form.validate()) {
        return
      }
      let self = this
      axiosBase
        .post('/signin', {
          email: self.email,
          password: self.password
        })
        .then(res => {
          this.snackOn({ payload: 'Sign in Success!', color: 'green' })
          this.setUserState(res.data.access_token)
          Cookies.set('access_token', res.data.access_token)
          Cookies.set('refresh_token', res.data.refresh_token)
          this.unsetSigninView()
          router.push('/home')
        })
        .catch(() => {
          this.snackOn({ payload: 'An error has occured', color: 'error' })
        })
    }
  }
}
</script>

<style scoped>
.v-divider {
  margin: 0px;
}
</style>
