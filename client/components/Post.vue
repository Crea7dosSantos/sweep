<template>
  <v-dialog v-model="postViewvisible" width="500px">
    <v-card dark>
      <input
        ref="postImage"
        style="display: none"
        type="file"
        accept="image/jpeg, image/jpg, image/png"
        @change="selectedPostImage()"
      />
      <v-card-title>
        <v-btn text icon @click="closeModal">
          <v-icon>clear</v-icon>
        </v-btn>
        <span class="close-profile">post window</span>
      </v-card-title>
      <v-divider />
      <p class="image-title body-2">select back image</p>
      <div class="image-div">
        <v-img v-show="uploadedPostImage" height="250" :src="uploadedPostImage">
          <v-row class="fill-height" align="center">
            <v-col justify="center" class="backimage-button">
              <v-btn icon text @click="uploadPostImage">
                <v-icon>add_a_photo</v-icon>
              </v-btn>
            </v-col>
            <v-col align-self="end" cols="12" class="avatar-col" />
          </v-row>
        </v-img>
      </div>
      <v-col cols="12" md="12">
        <v-text-field
          v-model="postTitle"
          filled
          counter="50"
          label="Title"
          placeholder="Post title"
        />
        <v-textarea v-model="postContent" filled label="Content" placeholder="Post content" />
      </v-col>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn color="red darken-1" text @click="closeModal">Cancel</v-btn>
        <v-btn color=" darken-1" text @click="savePost">Post</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import AWS from 'aws-sdk'
import S3 from 'aws-sdk/clients/s3'
import Axios from 'axios'
import Cookies from 'js-cookie'

export default {
  data() {
    return {
      uploadedPostImage:
        'https://cdn.vuetifyjs.com/images/parallax/material.jpg',
      postImageSetKey: '',
      isSetPostImage: false,
      postTitle: '',
      postContent: ''
    }
  },
  computed: {
    ...mapState('modal', ['isPostView']),
    ...mapState('user', ['user']),
    postViewvisible: {
      get() {
        return this.isPostView
      },
      set() {
        this.$store.dispatch('modal/unsetPostView')
        this.deleteData()
      }
    }
  },
  methods: {
    ...mapActions('modal', ['unsetPostView']),
    closeModal: function() {
      this.unsetPostView()
      this.deleteData()
    },
    savePost: function() {
      const self = this
      let dict = {
        title: self.postTitle,
        content: self.postContent,
        post_image_key: self.postImageSetKey
      }
      if (self.isSetPostImage == false) {
        const key = this.getRandomImageKey()
        dict['post_image_key'] = key
      }
      this.axiosAccessHandler()
        .post('/create', dict)
        .then(() => {
          self.closeModal()
        })
        .catch(err => {
          console.log(err)
        })
    },
    uploadPostImage: function() {
      this.$refs.postImage.click()
    },
    getPostImageBucket: function() {
      const postImageBucketName = process.env.POST_IMAGE_BUCKET_NAME
      const s3 = new S3({
        params: { Bucket: postImageBucketName, Region: 'ap-northeast-1' }
      })
      return s3
    },
    selectedPostImage: function() {
      const file = this.$refs.postImage.files[0]
      if (!file) {
        return
      }
      const postImageAccessKeyId = process.env.POST_IMAGE_ACCESS_KEY_ID
      const postImageSecretAccessKey = process.env.POST_IMAGE_SECRET_ACCESS_KEY
      AWS.config.update({
        accessKeyId: postImageAccessKeyId,
        secretAccessKey: postImageSecretAccessKey
      })
      const s3 = this.getPostImageBucket()
      s3.putObject(
        {
          Key: file.name,
          ContentType: file.type,
          Body: file,
          ACL: 'public-read'
        },
        function(err, data) {
          if (data !== null) {
            console.log('success post image save')
            console.log(data)
          } else {
            console.log('error だよ')
            console.log(err)
          }
        }
      )
      this.createImage(file)
    },
    createImage: function(file) {
      this.isSetPostImage = true
      let reader = new FileReader()
      this.postImageSetKey = file.name
      reader.onload = e => {
        this.uploadedPostImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    axiosAccessHandler: function() {
      const axiosAccess = Axios.create({
        baseURL: 'http://localhost:5000',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer ' + this.getToken()
        },
        responseType: 'json'
      })
      return axiosAccess
    },
    getToken: function() {
      return Cookies.get('access_token')
    },
    getRandomImageKey: function() {
      const randomFloor = Math.floor(Math.random() * 11)
      const randomString = String(randomFloor)
      const setKey = 'random-free-upload'
      const setExtension = '.jpg'
      const key = setKey + randomString + setExtension
      return key
    },
    deleteData: function() {
      this.postTitle = ''
      this.postContent = ''
      this.uploadedPostImage =
        'https://cdn.vuetifyjs.com/images/parallax/material.jpg'
      this.postImageSetKey = ''
      this.isSetPostImage = false
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
  padding-top: 80px;
}
.profile {
  padding-left: 5px;
}
.avatar-col {
  padding-left: 24px;
}
.image-title {
  padding-top: 15px;
  padding-left: 15px;
  margin-bottom: 5px;
  color: lightgray;
}
.image-div {
  border-radius: 5px;
  border: 2px solid gray;
  margin: 0 10px;
}
</style>
