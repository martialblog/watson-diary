<template>
  <v-container fluid>
    <h4>Reports</h4>

    <v-layout row wrap>
      <v-flex xs12>
        <v-alert warning dismissible v-model="noresults">
          No results
        </v-alert>
      </v-flex>
    </v-layout>

      <v-layout row wrap>

      <v-flex xs4>
        <v-subheader>Search Reports for User</v-subheader>
     </v-flex>
      <v-flex xs12 sm5>
        <v-text-field
          prepend-icon="search"
          name="username"
          label="Username"
          single-line
          v-model="searchfor"
          @keyup.native.enter="get_reports(searchfor)"
          ></v-text-field>
      </v-flex>
    </v-layout>

    <v-data-table
      v-bind:headers="headers"
      v-bind:items="items"
      v-model="selected"
      selected-key="date"
      select-all
      class="elevation-1"
      >
      <template slot="headers" scope="props">
        <span v-tooltip:bottom="{ 'html': props.item.text }">
          {{ props.item.text }}
        </span>
      </template>
      <template slot="items" scope="props">
        <td>
          <v-checkbox
            primary
            hide-details
            v-model="props.selected"
            ></v-checkbox>
        </td>
        <td>{{ props.item.username }}</td>
        <td class="text-xs-right">{{ props.item.date }}</td>
        <td class="text-xs-right">{{ props.item.reports }}</td>
      </template>
    </v-data-table>

    <v-layout row wrap>
      <v-flex xs12 class="text-xs-right">
        <v-btn error
               light
               v-if="selected.length > 0"
               @click.native="delete_reports"
               >Delete</v-btn>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        noresults: false,
        searchfor: '',
        selected: [],
        headers: [
          {
            text: 'Username',
            left: true,
            sortable: false,
            value: 'username'
          },
          { text: 'Date', value: 'date' },
          { text: 'Data', value: 'reports' },
        ],
        items: []
      }
    },
    methods: {
      get_reports: function (username) {
        this.$http.get('http://localhost:5000/reports/' + username).then(function(data){
          this.noresults = false;
          this.items = [];

          if (data.status == 204){
            this.noresults = true;
            return
          }

          for (var report of data.body) {
            var d = JSON.stringify(report.reports);
            report.reports = d.substring(0,100);
            this.items.push(report);
          }
        })
      },
      delete_reports: function() {
        for (var report of this.selected) {
          var index = this.items.map(elem => elem.date).indexOf(report.date);

          if (index > -1) {
            this.items.splice(index, 1);
          };

          var username = this.items[index].username;
          var date = this.items[index].date;

          this.$http.delete('http://localhost:5000/reports/' + username + "/" + date).then(function(data){
            console.log(name);
        });
        }
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
