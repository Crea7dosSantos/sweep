<template>
  <div>
    <v-app class="inspire">
      <div>
        <v-navigation-drawer v-model="drawer" absolute temporary>
          <v-list :class="{ 'is-hidden': !isAuthenticated }">
            <v-list-item>
              <v-list-item-avatar>
                <img src="~/assets/cristiano.jpg" />
              </v-list-item-avatar>
              <v-list-item-title>{{ user.name }}</v-list-item-title>
            </v-list-item>
          </v-list>
          <v-list>
            <v-text-field
              clearable
              flat
              label="Search"
              prepend-inner-icon="search"
              solo
              single-line
              hide-details
            />
          </v-list>
          <v-list class="pt-0" dense>
            <v-divider />
            <v-list-item-group v-for="item in items1" :key="item.title" link>
              <v-list-item :to="item.title">
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
            <v-divider />
            <v-list-item-group
              v-for="item in items2"
              :key="item.title"
              :class="{ 'is-hidden': !isAuthenticated }"
              link
            >
              <v-list-item :to="item.title">
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
            <v-list-item-group
              v-for="item in items3"
              :key="item.title"
              :class="{ 'is-hidden': isAuthenticated }"
              link
            >
              <v-list-item :to="item.title">
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-navigation-drawer>
        <v-toolbar dark color="grey darken-3">
          <v-app-bar-nav-icon class="hidden-md-and-up" @click.stop="drawer = !drawer" />
          <v-toolbar-items>
            <v-btn text to="/">Top</v-btn>
          </v-toolbar-items>
          <v-toolbar-items v-for="item in items1" :key="item.title" class="hidden-sm-and-down">
            <v-btn text :to="item.title">{{ item.title }}</v-btn>
          </v-toolbar-items>
          <v-spacer />
          <v-expand-x-transition>
            <v-text-field
              v-show="showSearchInput"
              class="hidden-sm-and-down"
              clearable
              flat
              label="Search"
              solo-inverted
              single-line
              hide-details
            />
          </v-expand-x-transition>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn icon @click="showSearchInput = !showSearchInput">
              <v-icon>search</v-icon>
            </v-btn>
          </v-toolbar-items>
          <v-toolbar-items v-for="item in items3" :key="item.title" class="hidden-sm-and-down">
            <v-btn text :class="{ 'is-hidden': isAuthenticated }" :to="item.title">{{ item.title }}</v-btn>
          </v-toolbar-items>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn text :class="{ 'is-hidden': !isAuthenticated }" to="user">{{ user.name }}</v-btn>
          </v-toolbar-items>
          <v-toolbar-items v-for="item in items2" :key="item.title" class="hidden-sm-and-down">
            <v-btn text :class="{ 'is-hidden': !isAuthenticated }" :to="item.title">{{ item.title }}</v-btn>
          </v-toolbar-items>
        </v-toolbar>
      </div>
      <div>
        <v-snackbar v-model="snackbarVisible" :color="actionStatus" top :timeout="timeout">
          {{ message }}
          <v-btn color="white" text @click="close">Close</v-btn>
        </v-snackbar>
      </div>
      <nuxt />
    </v-app>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['user']),
    ...mapGetters('user', ['isAuthenticated']),
    ...mapState('snackbar', ['message', 'isEnable', 'actionStatus']),
    snackbarVisible: {
      get() {
        return this.isEnable
      },
      set() {
        return this.$store.dispatch('snackbar/snackOff')
      }
    }
  },
  data: () => ({
    showSearchInput: false,
    drawer: false,
    snackbar: false,
    timeout: 3000,
    items1: [
      { title: 'home', icon: 'person' },
      { title: 'documentation', icon: 'dashboard' }
    ],
    items2: [{ title: 'signout', icon: 'dashboard' }],
    items3: [
      { title: 'signup', icon: 'account_box' },
      { title: 'signin', icon: 'gavel' }
    ]
  }),
  methods: {
    ...mapActions('snackbar', ['snackOff']),
    close: function() {
      this.snackOff()
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
