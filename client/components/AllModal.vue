<template>
  <div>
    <Signin />
    <signup />
    <Signout />
    <Post />
  </div>
</template>

<script>
import Signin from '~/components/Signin'
import Signup from '~/components/Signup'
import Signout from '~/components/Signout'
import Post from '~/components/Post'

export default {
  components: {
    Signin,
    Signup,
    Signout,
    Post
  }
}
</script>
