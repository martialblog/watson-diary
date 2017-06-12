<template>
  <v-container fluid>
    <h4>Users</h4>
    <v-list three-line>
      <template v-for="item in users">
        <v-subheader v-if="item.header" v-text="item.header"></v-subheader>
        <v-divider v-else-if="item.divider" v-bind:inset="item.inset"></v-divider>
        <v-list-item v-else v-bind:key="item.username">
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title v-html="item.username"></v-list-tile-title>
              <v-list-tile-sub-title v-html="item.mail"></v-list-tile-sub-title>
              <v-list-tile-sub-title v-html="item.feeds"></v-list-tile-sub-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-btn icon @click.native="delete_user(item.username)"><v-icon class="red--text text--lighten-1">close</v-icon></v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list-item>
      </template>
    </v-list>

    <v-layout row>
      <v-flex xs12 class="text-xs-right">
        <v-dialog v-model="dialog">
          <v-btn primary light slot="activator">Add User</v-btn>
          <v-card>
            <v-card-row>
              <v-card-title>New User</v-card-title>
            </v-card-row>
            <v-card-row>
              <v-card-text>
                <v-text-field label="Username" required v-model="newUser.username"></v-text-field>
                <v-text-field label="Email" required v-model="newUser.mail"></v-text-field>
                <v-text-field label="Password" type="password" required v-model="newUser.password"></v-text-field>
                <v-text-field v-for="feed in feeds"
                              v-bind:key="feed.id"
                              v-bind:data="feed.name"
                              name="feed.name"
                              :label="feed.name"
                              id="feed.name"
                              ></v-text-field>
              </v-card-text>
            </v-card-row>
            <v-card-row actions>
              <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Close</v-btn>
              <v-btn class="blue--text darken-1" flat @click.native="create_user">Create</v-btn>
            </v-card-row>
          </v-card>
        </v-dialog>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false,
        feeds: [],
        users: [],
        newUser: {
          username: '',
          mail: '',
          password: '',
          feeds: {
          }
        }
      }
    },
    methods: {
      delete_user: function (username) {
        this.$http.delete('http://localhost:5000/users/' + username).then(function(data){
          console.log(data);

          var index = this.users.map(elem => elem.username).indexOf(username);

          if (index > -1) {
            this.users.splice(index, 1);
          };

        })
      },
      create_user: function () {
        this.dialog = false;
        this.users.push(this.newUser);
        this.$http.put('http://localhost:5000/users/' + this.newUser.username, {

          username: this.newUser.username,
          mail: this.newUser.mail,
          password: this.newUser.password,
          feeds: this.newUser.feeds

        }).then(function(data){
          console.log(data);
        })
      }
    },
    created () {
      this.$http.get('http://localhost:5000/users').then(function(data){
        this.users = data.body;
      });
      this.$http.get('http://localhost:5000/feeds').then(function(data){
        this.feeds = data.body;
      });
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
