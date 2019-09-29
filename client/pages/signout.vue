<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col sm="7" md="4" lg="3">
            <v-card class="elevation-12">
              <div class="card-container">
                <div class="inner-icon">
                  <v-icon color="purple darken-2" size="50">swap_horiz</v-icon>
                </div>
                <div class="inner-recomend">
                  <span class="recomend-signout">Todo-Sampleからサインアウトしますか？</span>
                  <v-card-text>いつでもサインインし直すことができます。新しくアカウントを作成するときは、サインアップからアカウントを作成してください。</v-card-text>
                </div>
                <v-card-actions>
                  <div class="flex-grow-1" />
                  <v-btn color="normal">Cancel</v-btn>
                  <div class="flex-grow-1" />
                  <v-btn color="indigo accent-2" :loading="loading" @click="signout">Sign out</v-btn>
                </v-card-actions>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
import Cookies from 'js-cookie'

export default {
  data: () => ({
    loading: false
  }),
  methods: {
    ...mapActions('user', ['unsetUserState']),
    ...mapActions('snackbar', ['snackOn']),
    signout: function() {
      const router = this.$router
      this.snackOn({ payload: 'Sign out complete', color: 'green' })
      this.loading = true
      Cookies.remove('access_token')
      Cookies.remove('refresh_token')
      this.unsetUserState()
      this.loading = false
      router.push('/')
    }
  }
}
</script>

<style>
.card-container {
  padding: 15px 5px;
}
.inner-icon {
  text-align: center;
}
.inner-recomend {
  text-align: center;
  margin-top: 10px;
}
.recomend-signout {
  font-size: 17px;
  font-weight: bold;
  color: gray;
}
</style>
