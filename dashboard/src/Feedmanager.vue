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
       <v-btn
         light
         primary
         @click.native="true"
         >Add Feed</v-btn>
     </v-flex>
   </v-layout>

</v-container>
</template>

<script>
  export default {
    data () {
      return {
        feeds: []
      }
    },
    methods: {
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
