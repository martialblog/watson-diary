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
      <v-flex xs12 class="text-md-center">
        <v-card class="mt-3" v-for="item in personality"
                :key="item.name"
                 v-if="item.data"
                >
          <v-card-row class="light-blue darken-1">
            <v-card-title>
              <span class="white--text">{{item.name}}</span>
              <v-spacer></v-spacer>
            </v-card-title>
          </v-card-row>

          <v-card-row>
            <v-card-text>
              {{item.data}}
            </v-card-text>
          </v-card-row>

        </v-card>
      </v-flex>
    </v-layout>


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
               >Details</v-btn>

        <v-btn success
               light
               @click.native="update_user"
               >Save</v-btn>
      </v-flex>
    </v-layout>



  </v-container>
</template>

<script>
  import PI from './personalityInterpreter.js';

  export default {
    data () {
      return {
        visible: false,
        personality: [],
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

      this.$http.get('http://localhost:5000/pireport/' + username).then(function(data){
        const interpreter = new PI();

        var pi = data.body[0].pi;
        var openn = {}
        var consc = {}
        var extra = {}
        var agree = {}
        var range = {}
        var needs = {}

        for (var per of pi.personality[0].children){
          openn[per.trait_id] = per.percentile;
        }

        for (var per of pi.personality[1].children){
          consc[per.trait_id] = per.percentile;
        }

        for (var per of pi.personality[2].children){
          extra[per.trait_id] = per.percentile;
        }

        for (var per of pi.personality[3].children){
          agree[per.trait_id] = per.percentile;
        }

        for (var per of pi.personality[4].children){
          range[per.trait_id] = per.percentile;
        }

        for (var per of pi.needs){
           needs[per.trait_id] = per.percentile;
        }

        this.personality.push (
          { name: "Agreeableness",
            data: interpreter.interpretAgreeableness(agree).join(" ")
          }
        );

        this.personality.push (
          { name: "Extraversion",
            data: interpreter.interpretExtraversion(extra).join("")
          }
        );

        this.personality.push (
          { name: "Openness",
            data: interpreter.interpretOpenness(open).join("")
          }
        );

        this.personality.push (
          { name: "Needs",
            data: interpreter.interpretNeeds(needs).join("")
          }
        );

        this.personality.push (
          { name: "Emotional Range",
            data: interpreter.interpretEmotionalRange(range).join("")
          }
        );

        this.personality.push (
          { name: "Conscientiousness",
            data: interpreter.interpretConscientiousness(consc).join("")
          }
        );

        console.log(this.personality);

      });

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
