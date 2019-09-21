<template>
  <v-dialog
    v-model="userViewVisible"
    width="500px"
  >
    <v-card dark>
      <v-card-title>
        <v-icon class="close-profile">
          clear
        </v-icon>profile edit
      </v-card-title>
      <v-img
        height="100%"
        src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"
      >
        <v-row
          align="start"
          class="fill-height"
        >
          <v-col
            align-self="start"
            class="pa-0"
            cols="12"
          >
            <v-avatar
              color="grey"
              size="164"
              tile
            >
              <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg" />
            </v-avatar>
          </v-col>
          <v-col class="py-0">
            <v-list-item
              color="rgba(0, 0, 0, .4)"
              dark
            >
              <v-list-item-content>
                <v-list-item-title class="title">
                  Marcus Obrien
                </v-list-item-title>
                <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
      </v-img>
      <v-col
        cols="12"
        md="12"
      >
        <v-text-field
          v-model="user.name"
          label="Name"
          placeholder="Username"
        />
      </v-col>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn
          color="green darken-1"
          text
          @click="dialog = false"
        >
          Disagree
        </v-btn>
        <v-btn
          color="green darken-1"
          text
          @click="dialog = false"
        >
          Agree
        </v-btn>
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
  margin-right: 10px;
}
</style>
