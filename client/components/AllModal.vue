<template>
  <div>
    <Signin />
    <signup />
    <Signout />
  </div>
</template>

<script>
import Signin from '~/components/Signin'
import Signup from '~/components/Signup'
import Signout from '~/components/Signout'

export default {
  components: {
    Signin,
    Signup,
    Signout
  }
}
</script>
