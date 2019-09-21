<template>
  <v-dialog v-model="userViewVisible" width="500px">
    <v-card dark>
      <v-card-title>
        <v-btn text icon>
          <v-icon>clear</v-icon>
        </v-btn>
        <span class="close-profile">profile edit</span>
      </v-card-title>
      <v-img src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg">
        <v-row class="fill-height" align="center">
          <v-col justify="center" class="backimage-button">
            <v-btn icon text>
              <v-icon>add_a_photo</v-icon>
            </v-btn>
          </v-col>
          <v-col align-self="end" cols="12" class="avatar-col">
            <v-btn height="100px" icon class="avatar-button">
              <v-avatar color="grey" size="100">
                <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg" />
              </v-avatar>
            </v-btn>
          </v-col>
        </v-row>
      </v-img>
      <v-col cols="12" md="12">
        <v-text-field v-model="user.name" label="Name" placeholder="Username" />
      </v-col>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn color="green darken-1" text @click="dialog = false">Disagree</v-btn>
        <v-btn color="green darken-1" text @click="dialog = false">Agree</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {}
  },
  computed: {
    ...mapState('modal', ['isUserView']),
    ...mapState('user', ['user']),
    userViewVisible: {
      get() {
        return this.isUserView
      },
      set() {
        return this.$store.dispatch('modal/unsetUserView')
      }
    }
  }
}
</script>

<style  scoped>
.close-profile {
  margin-left: 18px;
  padding-bottom: 4px;
}
.backimage-button {
  text-align: center;
  padding-top: 120px;
}
.profile {
  padding-left: 5px;
}
.avatar-col {
  padding-left: 24px;
}
.avatar-button {
  padding-left: 52px;
}
</style>
