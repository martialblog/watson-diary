<template>
  <v-container fluid>

    <transition name="fade">
      <v-alert success v-bind:value="visible">
        Saved
      </v-alert>
    </transition>

    <v-card>
      <v-card-row class="light-blue darken-4">
        <v-card-title>
          <span class="white--text">{{username}}</span>
          <v-spacer></v-spacer>
        </v-card-title>
      </v-card-row>

      <v-card-row>
        <v-card-text>
          <v-text-field label="Email" required v-model="mail"></v-text-field>
          <v-text-field label="Password" type="password" required v-model="password"></v-text-field>
          <v-text-field v-for="feed in feeds"
                        v-bind:key="feed.key"
                        v-bind:data="feed.username"
                        name="feed.key"
                        :value="feed.username"
                        :label="feed.key"
                        id="feed.key"
                        ></v-text-field>
        </v-card-text>
      </v-card-row>
    </v-card>

    <v-layout row wrap>
      <v-flex xs12 class="text-xs-right">

        <v-dialog v-model="dialog">
          <v-btn primary light slot="activator">Add Feed</v-btn>
          <v-card>
            <v-card-title>New Feed</v-card-title>
            <v-divider></v-divider>
            <v-card-row height="200px">
              <v-card-text>

                <v-select
                  v-bind:items="availableFeeds"
                  v-model="newFeed.key"
                  label="Feed"
                  dark
                  single-line
                  auto
                  ></v-select>

                <v-text-field label="Username" required v-model="newFeed.username"></v-text-field>
              </v-card-text>
            </v-card-row>
            <v-card-row actions>
              <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Close</v-btn>
              <v-btn class="blue--text darken-1" flat @click.native="add_feed">Add</v-btn>
            </v-card-row>
          </v-card>
        </v-dialog>

        <v-btn info
               light
               router
               :to="diary(username)"
               >Diary</v-btn>

        <v-btn success
               light
               @click.native="update_user"
               >Save</v-btn>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        visible: false,
        availableFeeds: [],
        dialog: false,
        newFeed: {
          key: "",
          username: ""
        },
        username: "",
        mail: "",
        password: "",
        feeds: []
      }
    },
    methods: {
      diary: function (username){
        return "/diary/" + username;
      },
      update_user: function (){
        this.$http.put('http://localhost:5000/users/' + this.username, {

          username: this.username,
          mail: this.mail,
          password: this.password,
          feeds: this.feeds

        }).then(function(data){
          console.log(data);
        })

        this.visible = true;
      },
      add_feed: function (){
        this.dialog = false;
        this.feeds.push({key: this.newFeed.key.text, username: this.newFeed.username});
      },
      fade_out: function() {
        setTimeout(() => (
          this.visible = false
        ), 2500);
      },
    },
    created () {

      this.$http.get('http://localhost:5000/feeds').then(function(data){
        for (var value of data.body){
          this.availableFeeds.push({text: value.key});
        }
      });

      var username = this.$route.params.username;
      this.$http.get('http://localhost:5000/users/' + username).then(function(data){

        var user = data.body[0];
        this.username = user.username;
        this.mail = user.mail;
        this.password = user.password;
        this.feeds = user.feeds;

      });
    },
    watch: {
      visible: 'fade_out',
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
