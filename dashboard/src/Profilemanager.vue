<template>
  <v-container fluid>
    <h4>{{username}}</h4>
          <v-card>
            <v-card-row>
              <v-card-text>
                <v-text-field label="Email" required v-model="mail"></v-text-field>
                <v-text-field label="Password" type="password" required v-model="password"></v-text-field>
                <v-text-field v-for="feed in feeds"
                              v-bind:key="feed.id"
                              v-bind:data="feed.name"
                              name="feed.name"
                              :label="feed.name"
                              id="feed.name"
                              ></v-text-field>
              </v-card-text>
            </v-card-row>
          </v-card>

          <v-layout row wrap>
            <v-flex xs12 class="text-xs-right">
              <v-btn info
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
        username: "",
        mail: "",
        password: "",
        feeds: {}
      }
    },
    methods: {
      update_user: function (){
        this.$http.put('http://localhost:5000/users/' + this.username, {

          username: this.username,
          mail: this.mail,
          password: this.password,
          feeds: this.feeds

        }).then(function(data){
          console.log(data);
        })
      }
    },
    created () {
      this.$http.get('http://localhost:5000/users/sherlock').then(function(data){

        var user = data.body[0];
        this.username = user.username;
        this.mail = user.mail;
        this.password = user.password;
        this.feeds = user.feeds;

      });
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
