<template>
  <div class="container">
    <v-app>
      <h3 class="title is-3">
        All Post
      </h3>
      <div>
        <v-col
          v-for="(post, index) in posts"
          :key="index"
        >
          <v-card
            max-width="400"
            class="mx-auto"
          >
            <v-img
              :src="'https://' + bucketName + baseURL + post.post_image_key"
              class="white--text"
              height="200px"
            >
              <v-card-title
                class="align-end fill-height"
                max-width="400"
              >
                {{ post["title"] }}
              </v-card-title>
            </v-img>
            <v-card-text>
              <span>{{ post["date_posted"] | dateFormat }}</span>
              <br>
              <span class="text--primary">
                <span>{{ post.content }}</span>
                <br>
              </span>
            </v-card-text>
          </v-card>
        </v-col>
      </div>
      <template>
        <AllModal />
        <User />
      </template>
    </v-app>
  </div>
</template>

<script>
import Cookies from 'js-cookie'
import { mapState, mapActions } from 'vuex'
import AllModal from '~/components/AllModal'
import User from '~/components/User'

export default {
  components: {
    AllModal,
    User
  },
  computed: {
    ...mapState('post', ['posts'])
  },
  data: function() {
    return {
      token: '',
      bucketName: process.env.POST_IMAGE_BUCKET_NAME,
      baseURL: process.env.BASE_URL
    }
  },
  mounted: function() {
    let self = this
    const router = this.$router
    if (!this.getAccessToken()) {
      self.displaySigninView()
      self.displaySnackOn('Please sign in', 'error')
      router.push('/')
      return
    }
    this.$store.dispatch(
      'post/init',
      this.getAccessToken(),
      this.getRefreshToken()
    )
  },
  methods: {
    ...mapActions('snackbar', ['snackOn']),
    ...mapActions('modal', ['setSigninView']),
    displaySnackOn: function(text, color) {
      this.snackOn({ payload: text, color: color })
    },
    displaySigninView: function() {
      this.setSigninView()
    },
    getAccessToken: function() {
      return Cookies.get('access_token')
    },
    getRefreshToken: function() {
      return Cookies.get('refresh_token')
    }
  }
}
</script>

<style>
.todo-list {
  margin-top: 50px;
}
.td-font {
  color: gray;
  font-size: 17px;
}
.table td {
  vertical-align: middle;
}
.new-todo {
  margin-top: 20px;
}
.create-part {
  background: lightgray;
}
.container {
  margin-top: 20px;
}
</style>
