<template>
  <div>
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
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['user']),
    ...mapGetters('user', ['isAuthenticated'])
  }
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
