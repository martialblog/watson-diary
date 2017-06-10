<template>
  <v-container fluid>
    <h4>Users</h4>
    <v-list three-line>
      <template v-for="item in items">
        <v-subheader v-if="item.header" v-text="item.header"></v-subheader>
        <v-divider v-else-if="item.divider" v-bind:inset="item.inset"></v-divider>
        <v-list-item v-else v-bind:key="item.title">
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title v-html="item.username"></v-list-tile-title>
              <v-list-tile-sub-title v-html="item.mail"></v-list-tile-sub-title>
              <v-list-tile-sub-title v-html="item.feeds"></v-list-tile-sub-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-list-tile-action-text>Delete</v-list-tile-action-text>
              <v-icon class="red--text text--lighten-1">close</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </v-list-item>
      </template>
    </v-list>

    <v-layout row justify-center>
      <v-dialog v-model="dialog">
        <v-btn primary light slot="activator">New User</v-btn>
        <v-card>
          <v-card-row>
            <v-card-title>User Profile</v-card-title>
          </v-card-row>
          <v-card-row>
            <v-card-text>
              <v-text-field label="Username" required></v-text-field>
              <v-text-field label="Email" required></v-text-field>
              <v-text-field label="Password" type="password" required></v-text-field>
              <v-text-field v-for="feed in feeds"
                            name="input-1"
                            :label="feed.name"
                            id="testing"
                            ></v-text-field>
            </v-card-text>
          </v-card-row>
          <v-card-row actions>
            <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Close</v-btn>
            <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Save</v-btn>
          </v-card-row>
        </v-card>
      </v-dialog>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
        feeds: [
          {name: "Twitter"},
          {name: "Facebook"},
          {name: "Mail"},
        ],
        items: [
          { username: 'moriarty', mail: 'mori@arty.se', password: "secret", feeds: {Facebook: "mori1966"}},
          { divider: true, inset: true },
          { username: 'sherlock', mail: 'sher@locked.co.uk', password: "secret", feeds: {Twitter: "sherlock"}},
          { divider: true, inset: true },
          { username: 'hansgruber', mail: 'hans@gruber.de', password: "secret", feeds: {Twitter: "grüber", Mail: "hansi"}}
        ]
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
