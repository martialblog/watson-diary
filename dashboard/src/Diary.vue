<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="purple darken-1 white--text mt-3">
        <div>{{ title }}</div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        title: 'Diary',
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
