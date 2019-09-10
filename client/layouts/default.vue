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
          :class="{ 'is-hidden': !isAuth }"
          to="/signout"
        >
          Sign out
        </n-link>
        <n-link
          class="navbar-item button is-primary default-button"
          :class="{ 'is-hidden': isAuth }"
          to="/signup"
        >
          Sign up
        </n-link>
        <n-link
          class="navbar-item button is-light has-text-grey-dark default-button"
          to="/signin"
          :class="{ 'is-hidden': isAuth }"
        >
          Sign in
        </n-link>
      </div>
    </nav>
    <nuxt />
  </div>
</template>

<script>
import Cookies from 'js-cookie'

export default {
  data: function() {
    return {
      isAuth: false
    }
  },
  beforeMount: function() {
    let token = Cookies.get('jwt_token')
    console.log('default.vue is before mount')
    if (token) {
      this.isAuth = true
      console.log('default.vue is before mount in token confirm')
    }
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
