<template>
  <v-container fluid>
    <h4>Reports</h4>
    <v-layout row wrap>
      <v-flex xs4>
        <v-subheader>Search Reports for User</v-subheader>
     </v-flex>
      <v-flex xs12 sm5>
        <v-text-field
          name="input-1-3"
          label="Username"
          single-line
          prepend-icon="search"
          ></v-text-field>
      </v-flex>
    </v-layout>

 <v-data-table
    v-bind:headers="headers"
    v-bind:items="items"
    v-bind:search="search"
    v-model="selected"
    selected-key="name"
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
      <td class="text-xs-right">{{ props.item.data }}</td>
    </template>
 </v-data-table>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        search: '',
        selected: [],
        headers: [
          {
            text: 'Username',
            left: true,
            sortable: false,
            value: 'username'
          },
          { text: 'Date', value: 'date' },
          { text: 'Data', value: 'data' },
        ],
        items: [
          {
            value: false,
            username: 'sherlock',
            date: '2017-04-04',
            data: "DATA OBJECT"
          },
          {
            value: false,
            username: 'moriarty',
            date: '2017-05-04',
            data: "DATA OBJECT"
          }
        ]
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
