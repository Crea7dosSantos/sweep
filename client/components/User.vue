<template>
  <v-dialog v-model="userViewVisible" width="500px">
    <v-card dark>
      <input
        style="display: none"
        ref="backImage"
        type="file"
        accept="image/jpeg, image/jpg, image/png"
        @change="selectedBackImage()"
      />
      <input
        style="display: none"
        ref="userImage"
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
      <v-img src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg">
        <v-row class="fill-height" align="center">
          <v-col justify="center" class="backimage-button">
            <v-btn icon text @click="uploadBackImage">
              <v-icon>add_a_photo</v-icon>
            </v-btn>
          </v-col>
          <v-col align-self="end" cols="12" class="avatar-col">
            <button height="100px" icon class="avatar-button" @click="uploadUserImage">
              <v-avatar color="grey" size="100">
                <v-img v-show="uploadImage" :src="uploadImage" />
              </v-avatar>
            </button>
          </v-col>
        </v-row>
      </v-img>
      <v-col cols="12" md="12">
        <v-text-field filled counter="25" label="Name" v-model="user.name" placeholder="Username" />
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

export default {
  data() {
    return {
      uploadImage: ''
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
  methods: {
    ...mapActions('modal', ['unsetUserView']),
    closeModal: function() {
      this.unsetUserView()
    },
    saveProfile: function() {},
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
      console.log('selectedBackImage')
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
      this.createImage(file)
    },
    selectedUserImage: function() {
      console.log('selectedUserImage')
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
          if (data !== null) {
            console.log(data)
          } else {
            console.log(err)
          }
        }
      )
    },
    createImage: function(file) {
      let reader = new FileReader()
      reader.onload = e => {
        this.uploadImage = e.target.result
      }
      reader.readAsDataURL(file)
      console.log('cretaeImage')
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
