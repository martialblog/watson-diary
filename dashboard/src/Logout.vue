<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="red darken-1 white--text mt-3">
        <div>{{ title }}</div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        title: 'Logout',
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
