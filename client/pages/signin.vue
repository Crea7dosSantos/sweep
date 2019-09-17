<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar flat>
                <v-toolbar-title class="grey--text">signIn form</v-toolbar-title>
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
                <v-btn color="primary" @click="signin">Sign in</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import axiosBase from '@/plugins/axiosBase'
import Cookies from 'js-cookie'
import { mapActions } from 'vuex'

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
  methods: {
    ...mapActions('user', ['signIn']),
    ...mapActions('snackbar', ['snackOn']),
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
          this.snackOn('Sign in complete')
          this.signIn(res.data.access_token)
          Cookies.set('access_token', res.data.access_token)
          Cookies.set('refresh_token', res.data.refresh_token)
          router.push('/home')
        })
        .catch(() => {
          this.snackOn('An error has occured')
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
