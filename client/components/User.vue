<template>
  <v-dialog v-model="userViewVisible" width="500px">
    <v-card dark>
      <input
        ref="backImage"
        style="display: none"
        type="file"
        accept="image/jpeg, image/jpg, image/png"
        @change="selectedBackImage()"
      />
      <input
        ref="userImage"
        style="display: none"
        type="file"
        accept="image/jpeg, image/jpg, image/png"
        @change="selectedUserImage()"
      />
      <v-card-title>
        <v-btn text icon @click="closeModal">
          <v-icon>clear</v-icon>
        </v-btn>
        <span class="close-profile">profile edit</span>
      </v-card-title>
      <v-img v-show="uploadedBackImage" height="300" :src="uploadedBackImage">
        <v-row class="fill-height" align="center">
          <v-col justify="center" class="backimage-button">
            <v-btn icon text @click="uploadBackImage">
              <v-icon>add_a_photo</v-icon>
            </v-btn>
          </v-col>
          <v-col align-self="end" cols="12" class="avatar-col">
            <button height="100px" icon class="avatar-button" @click="uploadUserImage">
              <v-avatar color="grey" size="100">
                <v-img v-show="uploadedUserImage" :src="uploadedUserImage" />
              </v-avatar>
            </button>
          </v-col>
        </v-row>
      </v-img>
      <v-col cols="12" md="12">
        <v-text-field v-model="user.name" filled counter="25" label="Name" placeholder="Username" />
      </v-col>
      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn color="red darken-1" text @click="closeModal">Cancel</v-btn>
        <v-btn color=" darken-1" text @click="saveProfile">Save</v-btn>
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
import UserDefault from '~/assets/user_default.png'

export default {
  data() {
    return {
      uploadedUserImage: '',
      uploadedBackImage: '',
      UserImageSetKey: false,
      BackImageSetKey: false
    }
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
  },
  mounted() {
    const self = this
    const baseURL = process.env.BASE_URL
    const userImageBucketName = process.env.USER_IMAGE_BUCKET_NAME
    const backImageBucketName = process.env.BACK_IMAGE_BUCKET_NAME
    this.axiosAccessHandler()
      .get('/profile')
      .then(res => {
        const data = res.data.user[0]
        data['profile_image_key'] == null
          ? (self.uploadedUserImage = UserDefault)
          : (self.uploadedUserImage = `https://${userImageBucketName}${baseURL}${
              data['profile_image_key']
            }`)
        data['profile_back_image_key'] == null
          ? (self.uploadedBackImage =
              'https://cdn.vuetifyjs.com/images/parallax/material.jpg')
          : (self.uploadedBackImage = `https://${backImageBucketName}${baseURL}${
              data['profile_back_image_key']
            }`)
      })
      .catch(() => {
        this.snackOn({ paylod: 'error get profile', color: 'error' })
        return
      })
  },
  methods: {
    ...mapActions('modal', ['unsetUserView']),
    ...mapActions('snackbar', ['snackOn']),
    closeModal: function() {
      this.unsetUserView()
    },
    saveProfile: function() {
      const self = this
      let dict = { profile_image_key: null, profile_back_image_key: null }
      if (self.UserImageSetKey !== false) {
        dict['profile_image_key'] = self.UserImageSetKey
      }
      if (self.BackImageSetKey !== false) {
        dict['profile_back_image_key'] = self.BackImageSetKey
      }
      this.axiosAccessHandler()
        .post('/save', dict)
        .then(() => {
          console.log('success update profile')
          this.snackOn({ payload: 'success update profile', color: 'green' })
          self.closeModal()
        })
        .catch(err => {
          this.snackOn({ payload: 'Failed to update profile', color: 'error' })
          console.log(err)
        })
    },
    uploadBackImage: function() {
      this.$refs.backImage.click()
    },
    uploadUserImage: function() {
      this.$refs.userImage.click()
    },
    getUserImageBucket: function() {
      const userImageBucketName = process.env.USER_IMAGE_BUCKET_NAME
      const s3 = new S3({
        params: { Bucket: userImageBucketName, Region: 'ap-northeast-1' }
      })
      return s3
    },
    getBackImageBucket: function() {
      const backImageBucketName = process.env.BACK_IMAGE_BUCKET_NAME
      const s3 = new S3({
        params: { Bucket: backImageBucketName, Region: 'ap-northeast-1' }
      })
      return s3
    },
    selectedBackImage: function() {
      const file = this.$refs.backImage.files[0]
      if (!file) {
        return
      }
      const backImageAccessKeyId = process.env.BACK_IMAGE_ACCESS_KEY_ID
      const backImageSecretAccessKey = process.env.BACK_IMAGE_SECRET_ACCESS_KEY
      AWS.config.update({
        accessKeyId: backImageAccessKeyId,
        secretAccessKey: backImageSecretAccessKey
      })
      const s3 = this.getBackImageBucket()
      s3.putObject(
        {
          Key: file.name,
          ContentType: file.type,
          Body: file,
          ACL: 'public-read'
        },
        function(err, data) {
          if (data === null) {
            console.log(err)
            return
          }
        }
      )
      this.createImage(file, 'backImage')
    },
    selectedUserImage: function() {
      const file = this.$refs.userImage.files[0]
      if (!file) {
        return
      }
      const userImageAccessKeyId = process.env.USER_IMAGE_ACCESS_KEY_ID
      const userImageSecretAccessKey = process.env.USER_IMAGE_SECRET_ACCESS_KEY
      AWS.config.update({
        accessKeyId: userImageAccessKeyId,
        secretAccessKey: userImageSecretAccessKey
      })
      const s3 = this.getUserImageBucket()
      s3.putObject(
        {
          Key: file.name,
          ContentType: file.type,
          Body: file,
          ACL: 'public-read'
        },
        function(err, data) {
          if (data === null) {
            console.log(err)
            return
          }
          console.log(data)
        }
      )
      this.createImage(file, 'userImage')
    },
    createImage: function(file, select) {
      let reader = new FileReader()
      if (select === 'userImage') {
        reader.onload = e => {
          this.UserImageSetKey = file.name
          this.uploadedUserImage = e.target.result
        }
      } else if (select === 'backImage') {
        reader.onload = e => {
          this.BackImageSetKey = file.name
          this.uploadedBackImage = e.target.result
        }
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
</style>
