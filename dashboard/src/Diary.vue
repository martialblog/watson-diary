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
            <template scope="{ save, cancel }">
              <v-card-row actions>
                <v-btn flat primary @click.native="cancel()">Cancel</v-btn>
                <v-btn flat primary @click.native="save()">Save</v-btn>
              </v-card-row>
            </template>
          </v-date-picker>
        </v-menu>
      </v-flex>

      <v-flex xs12>
        <v-card class="mt-3">
          <v-card-text>{{date}} - {{text}}</v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs12 class="text-md-center">
        <v-card class="mt-3">
          <v-card-text>
            <svg id="#chart" style='height:600px; width:600px'></svg>
          </v-card-text>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import * as nv from 'nvd3';

export default {
  data () {
    return {
      menu: false,
      date: null,
      availableDates: [],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eu dapibus mi. In et auctor velit, nec pretium massa. Nunc rutrum metus tincidunt efficitur accumsan. Proin ut turpis at mauris accumsan ullamcorper vel vitae quam. Sed nunc augue, rutrum vitae tincidunt ut, congue porttitor quam. Donec semper, purus at sagittis tincidunt, ex tellus ullamcorper mi, a consequat libero risus id metus. Nam justo justo, tincidunt in congue ut, tristique ut quam. Donec vitae rutrum risus, in convallis tortor. Nam scelerisque gravida gravida. Maecenas nec massa in purus finibus dignissim. Proin finibus, odio id vehicula condimentum, neque velit rhoncus lorem, nec facilisis magna massa et nisi. Nulla posuere tristique ante, vehicula convallis ipsum egestas id. Mauris at fringilla lectus, vel sollicitudin sapien. Vivamus semper sodales ligula, laoreet egestas dolor mollis non. Morbi tincidunt augue odio, a molestie massa aliquet molestie.',
    }
  },
  created () {
    // var today = new Date().toISOString().substring(0, 10);
    this.$http.get('http://localhost:5000/reports/sherlock').then(function(data){
        for (var value of data.body){
          this.availableDates.push(value.date);
          this.date = value.date;
        }
    });
  },
  methods: {
    save: function () {
      console.log(this.date);
      // TODO: API Call. Get report for date
    }
  },
  mounted() {

    function exampleData() {
      return  [
        {
          "label": "Anger",
          "value" : 29.765957771107
        } ,
        {
          "label": "Disgust",
          "value" : 50.0
        } ,
        {
          "label": "Fear",
          "value" : 32.807804682612
        } ,
        {
          "label": "Joy",
          "value" : 96.45946739256
        } ,
        {
          "label": "Sadness",
          "value" : 50.19434030906893
        } ]}

    nv.addGraph(function() {

      var chart = nv.models.pieChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .showLabels(true)
          .labelThreshold(.05)
          .labelType("percent")
          .donut(true)
          .donutRatio(0.35)
      ;

      d3.select("svg")
        .datum(exampleData())
        .transition().duration(350)
        .call(chart);

      return chart;
    });

  }
}
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
