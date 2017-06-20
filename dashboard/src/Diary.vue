<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 class="text-md-center">
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


      <v-flex xs12 class="text-md-center">
        <v-card class="mt-3">
          <v-card-text>
            <chart
              :chart-data="chartreport"
              :options="chartoptions"
              ></chart>
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12>
        <v-card class="mt-3">
          <v-card-text>{{text}}</v-card-text>
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
      text: '',
      menu: false,
      date: null,
    }
  },
  created () {
    this.$http.get('http://localhost:5000/reports/sherlock').then(function(data){
        for (var value of data.body){
          this.availableDates.push(value.date);
          this.date = value.date;
        }
    });
  },
  methods: {
    save_date: function() {
      this.menu = false;
      this.get_report();
    },
    fill_chartdata: function (data) {
      var labels = [];
      var values = [];

      for (var emotion of data){
        labels.push(emotion.tone_name);
        values.push(emotion.score*100);
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
    fill_text: function () {
      this.text = Lorem({
        count: 30
      })
    },
    get_report: function () {

      var ta_report = null;

      this.$http.get('http://localhost:5000/reports/sherlock/' + this.date).then(function(data){

        for (var value of data.body){
          ta_report = value.reports[0].ta.document_tone.tone_categories[0].tones;
        }
        this.fill_chartdata(ta_report);
        this.fill_text();
      });
    }
  }
}
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
