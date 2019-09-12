<template>
  <div>
    <button class="button is-praimary" @click="signout">Sign out</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import Cookies from 'js-cookie'

export default {
  methods: {
    ...mapActions('user', ['signOut']),
    signout: function() {
      Cookies.remove('jwt_token')
      this.signOut()
    }
  }
}
</script>
