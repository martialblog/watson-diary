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

    <v-layout row>
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
            <v-chip label class="pink white--text" v-for="item in keywords" :key="item.text">
              <v-icon left>label</v-icon>
              {{ item.text }}
            </v-chip>
            <h5 v-if="entities.length > 0">Entities</h5>
            <v-chip class="indigo white--text" v-for="item in entities" :key="item.text">
              <v-avatar>
                <v-icon>account_circle</v-icon>
              </v-avatar>
                {{ item.text }}
            </v-chip>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>


    <v-layout row wrap>
      <v-flex xs12 class="text-md-center">
        <v-card class="mt-3">
          <v-card-text>
            <linechart
              :chart-data="linechartreport"
              :options="chartoptions"
              ></linechart>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs12>
        <v-card class="mt-3">
          <v-card-text>
           <v-text-field
             name="chatbot-input"
             single-line
             prepend-icon="micro"
             v-model="chatinput"
             @keyup.native.enter="post_chatbot()"
             ></v-text-field>
           <span v-for="item in reverseItems" :key="item.text">
             <v-chip v-if="item.type === 'question'" label class="blue white--text">
               {{item.text}}
             </v-chip>
             <v-chip v-if="item.type === 'answer'" label class="red white--text">
               {{item.text}}
             </v-chip>
             <br>
           </span>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
export default {
  data () {
    return {
      username: null,
      chatinput: "",
      chatprotocol: [],
      chatsessionid: '',
      availableDates: [],
      chartoptions: {responsive: true, maintainAspectRatio: false},
      linechartreport: {
        labels: [],
        datasets: [
        ]},
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
    this.chatsessionid = Date.now();
    this.username = this.$route.params.username;

    this.$http.get('http://localhost:5000/reports/' + this.username).then(function(data){
      for (var value of data.body){
        this.availableDates.push(value.date);
        this.date = value.date;
      }
      this.get_report();
      this.fill_linechart(data);
    });

    this.$http.post('http://localhost:5000/functions/chatbot', {
      sessionid: this.chatsessionid,
      input: ""
    })

  },
  computed: {
    reverseItems() {
      return this.chatprotocol.slice().reverse();
    }
  },
  methods: {
    post_chatbot: function() {
      this.chatprotocol.push(
        {'type': 'question', 'text': this.chatinput}
      )

      this.$http.post('http://localhost:5000/functions/chatbot', {
        sessionid: this.chatsessionid,
        input: this.chatinput
      }).then(function(data){
        this.chatprotocol.push(
          {'type': 'answer', 'text': data.body[0].text.toString()}
        );
      })

      this.chatinput = "";
    },
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
          emotion = value.reports.nlu.emotion.document.emotion;
          keywords = value.reports.nlu.keywords
          entities = value.reports.nlu.entities;
        }

        this.fill_chartdata(emotion);
        this.fill_keywords(keywords);
        this.fill_entities(entities);
      });
    },
    fill_linechart: function (data) {
      var labels = []
      var anger = []
      var fear = []
      var disgust = []
      var joy = []
      var sadness = []

      for (var value of data.body){
        labels.push(value.date);
        fear.push(value.reports.nlu.emotion.document.emotion['fear'] * 100);
        sadness.push(value.reports.nlu.emotion.document.emotion['sadness'] * 100);
        anger.push(value.reports.nlu.emotion.document.emotion['anger'] * 100);
        joy.push(value.reports.nlu.emotion.document.emotion['joy'] * 100);
        disgust.push(value.reports.nlu.emotion.document.emotion['disgust'] * 100);
      }

      var datasets = {
        labels: labels,
        datasets: [
        {
          label: 'Anger',
          fill: false,
          borderColor: '#b71c1c',
          data: anger
        },
        {
          label: 'Disgust',
          fill: false,
          borderColor: '#2e7d32',
          data: disgust
        },
        {
          label: 'Fear',
          fill: false,
          borderColor: '#4527a0',
          data: fear
        },
        {
          label: 'Sadness',
          fill: false,
          borderColor: '#1e88e5',
          data: sadness
        },
        {
          label: 'Joy',
          fill: false,
          borderColor: '#ef6c00',
          data: joy
        }]
      };

      this.linechartreport = datasets;

    }
  }
}
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
