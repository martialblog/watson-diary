<template>
  <v-container fluid>
    <h4>Feeds</h4>
    <v-layout row wrap>
      <v-flex xs12 md6>
        <v-subheader>Available Feeds</v-subheader>
        <v-card class="elevation-0">
          <v-card-text>
            <v-switch v-for="feed in feeds"
                      :label="feed.name"
                      v-model="feed.active"
                      v-bind:key="feed.key"
                      :value="feed.active"
                      success
                      dark
                      @click.native="toggle_feed(feed.key)"
                      ></v-switch>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

   <v-layout row wrap>
     <v-flex xs12 class="text-xs-right">
        <v-dialog v-model="dialog" width="450">
          <v-btn primary light slot="activator">Add Feed</v-btn>
          <v-card>
            <v-card-row>
              <v-card-title>New Feed</v-card-title>
            </v-card-row>
            <v-card-row>
              <v-card-text>
                <v-text-field label="Name" required v-model="newFeed.name"></v-text-field>
                <v-text-field label="Key" required v-model="newFeed.key"></v-text-field>
                <v-text-field label="URL" required v-model="newFeed.url"></v-text-field>
                <v-text-field label="Date Field" required v-model="newFeed.date_field"></v-text-field>
                <v-text-field label="Text Field" required v-model="newFeed.text_field"></v-text-field>
              </v-card-text>
            </v-card-row>
            <v-card-row actions>
              <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Close</v-btn>
              <v-btn class="blue--text darken-1" flat @click.native="create_feed">Create</v-btn>
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
        newFeed: {
          key: '',
          url: '',
          name: '',
          date_field: '',
          text_field: '',
          active: false
        }
      }
    },
    methods: {
      create_feed: function() {
        this.dialog = false;
        this.feeds.push(this.newFeed);

        this.$http.put('http://localhost:5000/feeds/' + this.newFeed.key, {

          key: this.newFeed.key,
          url: this.newFeed.url,
          name:  this.newFeed.name,
          active:  this.newFeed.active,
          date_field:  this.newFeed.date_field,
          text_field:  this.newFeed.text_field

        }).then(function(data){
          console.log(data);
        })

      },
      toggle_feed: function (k) {

        var index = this.feeds.map(elem => elem.key).indexOf(k);

        if (index > -1) {
          this.$http.put('http://localhost:5000/feeds/' + k, {

            key: k,
            name: this.feeds[index].name,
            active: Boolean(this.feeds[index].active),
            date_field: "created_at",
            text_field: "text"

          }).then(function(data){
            console.log(data);
          })
        }

      }
    },
    created () {
      this.$http.get('http://localhost:5000/feeds').then(function(data){
        this.feeds = data.body;
      });
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
