<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar flat>
                <v-toolbar-title class="grey--text">SignIn form</v-toolbar-title>
                <div class="flex-grow-1" />
              </v-toolbar>
              <v-divider />
              <v-card-text>
                <v-form>
                  <v-text-field label="Email" name="Email" prepend-icon="email" type="text" />

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <div class="flex-grow-1" />
                <v-btn color="primary">Sign in</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  props: {},
  data: () => ({
    drawer: null
  })
}
</script>

<style scoped>
.v-divider {
  margin: 0px;
}
</style>
