<template>
  <section class="hero has-background-grey-lighter is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column" />
          <div class="column card box is-two-fifths">
            <div class="field form-title">
              <h3 class="title is-2 has-text-dark">Sign in</h3>
            </div>
            <div class="field">
              <label class="label">Email</label>
              <input class="input is-medium" type="email" placeholder="Email" />
            </div>
            <div class="field">
              <label class="label">Password</label>
              <input type="password" class="input is-medium" placeholder="Password" />
            </div>
            <div class="columns">
              <div class="column is-half"></div>
              <div class="column form-subject">
                <button class="button is-light">Cancel</button>
              </div>
              <div class="column form-subject">
                <div class="field">
                  <button class="button is-dark signin">Sign in</button>
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
  padding-right: 20px;
  padding-left: 20px;
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
  height: 40px;
}
.is-light {
  float: right;
}
</style>
