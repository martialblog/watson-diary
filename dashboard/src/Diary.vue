y<template>
  <v-container fluid>

    <v-layout row wrap>
      <v-flex xs6 class="text-md-center">
          <v-menu
          lazy
          :close-on-content-click="false"
          v-model="menu"
          transition="v-scale-transition"
          offset-y
          :nudge-left="40"
          >
          <v-text-field
            slot="activator"
            label="Select Date"
            v-model="date"
            prepend-icon="event"
            readonly
          ></v-text-field>
          <v-date-picker
            v-model="date"
            no-title
            scrollable
            actions
            :allowed-dates="availableDates">
            <template scope="{cancel}">
              <v-card-row actions>
                <v-btn flat primary @click.native="cancel">Cancel</v-btn>
                <v-btn flat primary @click.native="save_date">Save</v-btn>
              </v-card-row>
            </template>
          </v-date-picker>
          </v-menu>

      </v-flex>
      <v-flex xs3 class="text-md-center">
        <v-btn outline class="indigo--text" @click.native="prev_date">Previous</v-btn>
      </v-flex>
      <v-flex xs3 class="text-md-center">
        <v-btn outline class="indigo--text" @click.native="next_date">Next</v-btn>
      </v-flex>
    </v-layout>

      <v-layout row wrap>
      <v-flex xs6 class="text-md-center">
        <h4>{{username}}</h4>
      </v-flex>
      <v-flex xs6 class="text-md-center">
      </v-flex>
      </v-layout>

    <v-layout row wrap>
      <v-flex xs6 class="text-md-center">
        <v-card class="mt-3">
          <v-card-text>
            <chart
              :chart-data="chartreport"
              :options="chartoptions"
              ></chart>
          </v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs6>
        <v-card class="mt-3">
          <v-card-row class="light-blue darken-4">
            <v-card-title>
              <span class="white--text">{{date}}</span>
              <v-spacer></v-spacer>
            </v-card-title>
          </v-card-row>
          <v-card-text>
            <h5 v-if="keywords.length > 0">Keywords</h5>
            <v-chip label class="pink white--text" v-for="item in keywords">
              <v-icon left>label</v-icon>
              {{ item.text }}
            </v-chip>
            <h5 v-if="entities.length > 0">Entities</h5>
            <v-chip class="indigo white--text" v-for="item in entities">
              <v-avatar>
                <v-icon>account_circle</v-icon>
              </v-avatar>
                {{ item.text }}
            </v-chip>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
import Lorem from 'lorem-ipsum';

export default {
  data () {
    return {
      username: null,
      availableDates: [],
      chartoptions: {responsive: true, maintainAspectRatio: false},
      chartreport: {
        labels: [],
        datasets: [
        {
          label: 'Today',
          backgroundColor: '#3D5AFE',
          data: []
        }]},
      keywords: [],
      entities: [],
      menu: false,
      date: null,
    }
  },
  created () {
    this.username = this.$route.params.username;

    this.$http.get('http://localhost:5000/reports/' + this.username).then(function(data){
        for (var value of data.body){
          this.availableDates.push(value.date);
          this.date = value.date;
        }
      this.get_report();
    });
  },
  methods: {
    next_date: function() {
      var index = this.availableDates.indexOf(this.date);
      this.date = this.availableDates[index + 1];
      this.get_report();
    },
    prev_date: function() {
      var index = this.availableDates.indexOf(this.date);
      this.date = this.availableDates[index - 1];
      this.get_report();
    },
    save_date: function() {
      this.menu = false;
      this.get_report();
    },
    fill_chartdata: function (data) {
      var res = Object.entries(data).map((value)=>(value));
      var labels = [];
      var values = [];

      for (var emotion of res){
        labels.push(emotion[0]);
        values.push(emotion[1]*100);
      }

      var d = {
        labels: labels,
        datasets: [
          {
            label: 'Today',
            backgroundColor: '#3D5AFE',
            data: values
          }]}

      this.chartreport = d;
    },
    fill_entities: function (data) {
      this.entities = data;
    },
    fill_keywords: function (data) {
      this.keywords = data;
    },
    get_report: function () {
      var emotion = null;
      var keywords = null;
      var entities = null;

      this.$http.get('http://localhost:5000/reports/' + this.username +'/'+ this.date).then(function(data){

        for (var value of data.body){
          console.log(value);
          emotion = value.reports[0].nlu.emotion.document.emotion;
          keywords = value.reports[0].nlu.keywords
          entities = value.reports[0].nlu.entities;
        }

        this.fill_chartdata(emotion);
        this.fill_keywords(keywords);
        this.fill_entities(entities);
      });
    }
  }
}
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
