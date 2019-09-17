<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar flat>
                <v-toolbar-title class="grey--text">SignUp form</v-toolbar-title>
                <div class="flex-grow-1" />
              </v-toolbar>
              <v-divider />
              <v-card-text>
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
                <v-btn color="primary" @click="signup">Sign up</v-btn>
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
import { mapActions } from 'vuex'

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
  methods: {
    ...mapActions('snackbar', ['snackOn']),
    signup: function() {
      const router = this.$router

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
          router.push('/signin')
        })
        .catch(error => {
          console.log(error)
          this.snackOn({ payload: 'Error create account' })
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
