<template>
  <v-container fluid>
    <h4>Feeds</h4>
    <v-layout row wrap>
      <v-flex xs12 md6>
        <v-subheader>Activated Feeds</v-subheader>
        <v-card class="elevation-0">
          <v-card-text>
            <v-switch v-for="feed in availableFeeds"
                      :label="feed.name"
                      v-model="activatedFeeds"
                      v-bind:key="feed.id"
                      :value="feed.id"
                      success
                      dark
                      ></v-switch>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
</v-container>
</template>

<script>
  export default {
    data () {
      return {
        availableFeeds: [
          {name: "Twitter", id: "twitter"},
          {name: "Facebook", id: "facebook"},
          {name: "Instagram", id: "instagram"},
          {name: "Mail", id: "mail"},
          {name: "SMS", id: "sms"}
        ],
        activatedFeeds: [],
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
