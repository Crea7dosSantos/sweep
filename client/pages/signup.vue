<template>
  <section class="hero has-background-grey-lighter is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column" />
          <div class="column card box is-half">
            <div class="field form-title">
              <h3 class="title is-2 has-text-grey-dark">Sign up</h3>
            </div>
            <div class="field">
              <label class="label">Username</label>
              <input v-model="userName" class="input is-medium" type="text" placeholder="Username" />
            </div>
            <div class="field">
              <label class="label">Email</label>
              <input v-model="email" class="input is-medium" type="email" placeholder="Email" />
            </div>
            <div class="field">
              <label class="label">Password</label>
              <input
                v-model="password"
                type="password"
                class="input is-medium"
                placeholder="Password"
              />
            </div>
            <div class />
            <div class="columns">
              <div class="column is-half" />
              <div class="column form-subject">
                <button class="button is-light">Cancel</button>
              </div>
              <div class="column form-subject">
                <div class="field">
                  <button class="button is-dark" @click="createAcount">Create Acount</button>
                </div>
                <v-app>
                  <v-color-picker></v-color-picker>
                </v-app>
              </div>
            </div>
          </div>
          <div class="column" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data: function() {
    return {
      userName: '',
      email: '',
      password: ''
    }
  },
  methods: {
    createAcount: function() {
      console.log(this.userName)
      console.log(this.email)
      console.log(this.password)
    }
  }
}
</script>

<style scoped>
.card {
  background: white;
  padding-right: 30px;
  padding-left: 30px;
}
.form-title {
  text-align: center;
  margin-bottom: 10px;
  height: 60px;
  padding-top: 10px;
}
.form-subject {
  padding-top: 20px;
  padding-bottom: 20px;
}
.form-subject button {
  padding-right: 20px;
  padding-left: 20px;
}
.is-light {
  float: right;
}
</style>
