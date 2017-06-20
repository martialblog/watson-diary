<template>
  <v-container fluid>

    <v-card>
      <v-card-text>
        <h4>Help</h4>
        <div>{{text}}</div>
      </v-card-text>
    </v-card>

    <v-card class="blue darken-1 white--text mt-3">
      <v-card-text>
        <h4 class="white--text">Even More Help</h4>
        <div>{{text}}</div>
      </v-card-text>
    </v-card>

</v-container>
</template>

<script>
  import Lorem from 'lorem-ipsum';

  export default {
    data () {
      return {
        text: ""
      }
    },
    created () {
      this.text = Lorem({
        count: 30
      })

    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
