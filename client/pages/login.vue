<template>
  <section class="hero is-primary is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column is-one-third" />
          <div class="column card box">
            <div class="field form-title">
              <h3 class="title is-2 has-text-dark">login</h3>
            </div>
            <div class="field">
              <input class="input is-medium" type="email" placeholder="Email" />
            </div>
            <div class="field">
              <input type="password" class="input is-medium" placeholder="Password" />
            </div>
            <div class="columns">
              <div class="column is-half"></div>
              <div class="column form-subject">
                <button class="button is-light">Cancel</button>
              </div>
              <div class="column form-subject">
                <div class="field">
                  <button class="button is-dark">Login</button>
                </div>
              </div>
            </div>
          </div>
          <div class="column" />
        </div>
      </div>
    </div>
  </section>
</template>


<style scoped>
.card {
  background: white;
  height: 300px;
}
.form-title {
  text-align: center;
  margin-bottom: 10px;
  height: 60px;
  padding-top: 10px;
}
.input {
  margin-top: 10px;
}
.form-subject {
  margin-top: 15px;
}
.form-subject button {
  width: 90px;
}
</style>
