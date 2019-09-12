<template>
  <div>
    <button
      class="button is-praimary"
      @click="signout"
    >
      Sign out
    </button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions('user', ['signOut']),
    signout: function() {
      this.signOut()
    }
  }
}
</script>
