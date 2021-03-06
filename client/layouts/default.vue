<template>
  <v-app class="inspire">
    <div>
      <v-navigation-drawer v-model="drawer" absolute temporary>
        <v-list-item-group :class="{ 'is-hidden': !isAuthenticated }">
          <v-list-item to="/user">
            <v-list-item-avatar>
              <v-img :src="userImage" />
            </v-list-item-avatar>
            <v-list-item-title>{{ user.name }}</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
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
          <v-btn text to="/" :class="{ 'is-hidden': isAuthenticated }">Top</v-btn>
        </v-toolbar-items>
        <v-toolbar-items v-for="item in items" :key="item.title" class="hidden-sm-and-down">
          <v-btn text :class="{ 'is-hidden': !isAuthenticated }" :to="item.title">{{ item.title }}</v-btn>
        </v-toolbar-items>
        <v-toolbar-items v-for="item in items1" :key="item.title" class="hidden-sm-and-down">
          <v-btn text :to="item.title">{{ item.title }}</v-btn>
        </v-toolbar-items>
        <v-toolbar-items v-for="item in items4" :key="item.title" class="hidden-sm-and-down">
          <v-btn
            text
            :class="{ 'is-hidden': !isAuthenticated }"
            @click="tmp(item.title)"
          >{{ item.title }}</v-btn>
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
          <v-btn
            text
            :class="{ 'is-hidden': isAuthenticated }"
            @click="tmp(item.title)"
          >{{ item.title }}</v-btn>
        </v-toolbar-items>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn
            text
            :class="{ 'is-hidden': !isAuthenticated }"
            @click="displayUserView"
          >{{ user.name }}</v-btn>
        </v-toolbar-items>
        <v-toolbar-items v-for="item in items2" :key="item.title" class="hidden-sm-and-down">
          <v-btn
            text
            :class="{ 'is-hidden': !isAuthenticated }"
            @click="tmp(item.title)"
          >{{ item.title }}</v-btn>
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
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import UserDefault from '~/assets/user_default.png'

export default {
  computed: {
    ...mapState('user', ['user']),
    ...mapGetters('user', ['isAuthenticated']),
    ...mapState('snackbar', ['message', 'isEnable', 'actionStatus']),
    ...mapState('modal', ['isSignoutView']),
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
    userImage: UserDefault,
    showSearchInput: false,
    drawer: false,
    snackbar: false,
    timeout: 3000,
    items: [{ title: 'home', icon: 'person' }],
    items1: [{ title: 'documentation', icon: 'dashboard' }],
    items2: [{ title: 'signout', icon: 'dashboard' }],
    items3: [
      { title: 'signup', icon: 'account_box' },
      { title: 'signin', icon: 'gavel' }
    ],
    items4: [{ title: 'post', icon: 'person' }]
  }),
  methods: {
    ...mapActions('snackbar', ['snackOff']),
    ...mapActions('modal', ['setUserView']),
    ...mapActions('modal', ['setSigninView']),
    ...mapActions('modal', ['setSignupView']),
    ...mapActions('modal', ['setSignoutView']),
    ...mapActions('modal', ['setPostView']),
    close: function() {
      this.snackOff()
    },
    displayUserView: function() {
      this.setUserView()
    },
    displaySignupVie: function() {
      this.setSignupView()
    },
    displaySigninView: function() {
      this.setSigninView()
    },
    displaySignoutView: function() {
      this.setSignoutView()
    },
    displayPostView: function() {
      this.setPostView()
    },
    tmp: function(data) {
      if (data === 'signout') {
        this.displaySignoutView()
      } else if (data === 'signin') {
        this.displaySigninView()
      } else if (data === 'signup') {
        this.displaySignupVie()
      } else if (data === 'post') {
        this.displayPostView()
      }
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
