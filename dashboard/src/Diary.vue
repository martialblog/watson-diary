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
            v-model="e3"
            prepend-icon="event"
            readonly
          ></v-text-field>
          <v-date-picker v-model="e3" no-title scrollable actions>
            <template scope="{ save, cancel }">
              <v-card-row actions>
                <v-btn flat primary @click.native="cancel()">Cancel</v-btn>
                <v-btn flat primary @click.native="save()">Save</v-btn>
              </v-card-row>
            </template>
          </v-date-picker>
        </v-menu>
      </v-flex>
       <v-flex xs6 class="text-md-center">
         <v-btn dark default class="btn--dark-flat-focused"><v-icon left dark>import_contacts</v-icon>Diary</v-btn>
       </v-flex>
       <v-flex xs6 class="text-md-center">
         <v-btn dark default class="btn--dark-flat-focused"><v-icon left dark>insert_chart</v-icon>Stats</v-btn>
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
  export default {
    data () {
      return {
        e3: null,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eu dapibus mi. In et auctor velit, nec pretium massa. Nunc rutrum metus tincidunt efficitur accumsan. Proin ut turpis at mauris accumsan ullamcorper vel vitae quam. Sed nunc augue, rutrum vitae tincidunt ut, congue porttitor quam. Donec semper, purus at sagittis tincidunt, ex tellus ullamcorper mi, a consequat libero risus id metus. Nam justo justo, tincidunt in congue ut, tristique ut quam. Donec vitae rutrum risus, in convallis tortor. Nam scelerisque gravida gravida. Maecenas nec massa in purus finibus dignissim. Proin finibus, odio id vehicula condimentum, neque velit rhoncus lorem, nec facilisis magna massa et nisi. Nulla posuere tristique ante, vehicula convallis ipsum egestas id. Mauris at fringilla lectus, vel sollicitudin sapien. Vivamus semper sodales ligula, laoreet egestas dolor mollis non. Morbi tincidunt augue odio, a molestie massa aliquet molestie.',
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>