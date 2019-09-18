<template>
  <div>
    <User />
    <Signin />
    <signup />
    <Signout />
  </div>
</template>

<script>
import User from '~/components/User'
import Signin from '~/components/Signin'
import Signup from '~/components/Signup'
import Signout from '~/components/Signout'

export default {
  components: {
    User,
    Signin,
    Signup,
    Signout
  }
}
</script>
