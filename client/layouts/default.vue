<template>
  <!-- <div>
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <n-link
          class="navbar-item"
          to="/"
        >
          Top
        </n-link>
      </div>
      <div
        id="navbarBasicExample"
        class="navbar-menu"
      >
        <div class="navbar-start">
          <n-link
            class="navbar-item"
            to="/home"
          >
            Home
          </n-link>
          <n-link
            class="navbar-item"
            to="/documentation"
          >
            Documentation
          </n-link>
        </div>
      </div>
      <div class="navbar-end">
        <n-link
          class="navbar-item button is-primary default-button"
          :class="{ 'is-hidden': !isAuthenticated }"
          to="/signout"
        >
          Sign out
        </n-link>
        <n-link
          class="navbar-item button is-primary default-button"
          :class="{ 'is-hidden': isAuthenticated }"
          to="/signup"
        >
          Sign up
        </n-link>
        <n-link
          class="navbar-item button is-light has-text-grey-dark default-button"
          to="/signin"
          :class="{ 'is-hidden': isAuthenticated }"
        >
          Sign in
        </n-link>
        {{ user.name }}
      </div>
    </nav>
    <nuxt />
  </div>-->
  <div>
    <v-app class="inspire">
      <div>
        <v-toolbar dark color="grey darken-3">
          <v-toolbar-title>TodoApp</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-expand-x-transition>
            <v-text-field
              class="hidden-sm-and-down"
              clearable
              flat
              label="Search"
              solo-inverted
              single-line
              hide-details
              v-show="showSearchInput"
            ></v-text-field>
          </v-expand-x-transition>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn icon @click="showSearchInput = !showSearchInput">
              <v-icon>search</v-icon>
            </v-btn>
            <v-btn text>signup</v-btn>
            <v-btn text>signin</v-btn>
            <v-btn text>signout</v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </div>
      <nuxt />
    </v-app>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['user']),
    ...mapGetters('user', ['isAuthenticated'])
  },
  data: () => ({
    showSearchInput: false
  })
}
</script>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}
*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
.default-button {
  margin-right: 20px;
  margin-top: 7px;
}
.navbar-end {
  vertical-align: middle;
}
</style>
