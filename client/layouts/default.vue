<template>
  <div>
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <n-link class="navbar-item" to="/">Todo</n-link>
      </div>
      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <n-link class="navbar-item" to="/">Home</n-link>
          <n-link class="navbar-item" to="/">Documentation</n-link>
        </div>
      </div>
      <div class="navbar-end">
        <n-link class="navbar-item button is-primary default-button" to="/signup">Sign up</n-link>
        <n-link
          class="navbar-item button is-light has-text-grey-dark default-button"
          to="/signin"
        >Sign in</n-link>
      </div>
    </nav>
    <nuxt />
  </div>
</template>

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
/* .button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}
.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}
.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}
.button--grey:hover {
  color: #fff;
  background-color: #35495e;
} */
.default-button {
  margin-right: 20px;
  margin-top: 7px;
}
.navbar-end {
  vertical-align: middle;
}
</style>
