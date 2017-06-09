<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="green darken-1 white--text mt-3">
        <div>{{ title }}</div>
      </v-card-text>
    </v-card>
    <h3>Manage Profile</h3>
    <h3>Manage Feeds</h3>
    <h3>View Reports</h3>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        title: 'User Profile',
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
