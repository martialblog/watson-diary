<template>
  <v-container fluid>
    <v-layout row >
      <v-flex xs7>
        <v-date-picker v-model="picker" landscape></v-date-picker>
      </v-flex>
      <v-flex xs5>
    <v-card>
      <v-card-text>
        <div>{{ text }}</div>
      </v-card-text>
    </v-card>
      </v-flex>
    </v-layout>

    <v-layout row class="mt-3">
      <v-flex xs12>
        <v-card height="500px">
          <v-bottom-nav
            absolute
            shift
            value="true"
            :class="{
                    'blue-grey': e2 === 1,
                    'teal': e2 === 2
                    }"
            >
            <v-btn flat light @click.native="e2 = 1" :value="e2 === 1">
              <span>Text</span>
              <v-icon>subject</v-icon>
            </v-btn>
            <v-btn flat light @click.native="e2 = 2" :value="e2 === 2">
              <span>Diagram</span>
              <v-icon>insert_chart</v-icon>
            </v-btn>
          </v-bottom-nav>
        </v-card>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        picker: null,
        active: null,
        text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In cursus sapien dui, at sollicitudin felis pellentesque vel. Curabitur lobortis, nibh ut aliquam malesuada, ante nisi lobortis purus, sed egestas justo urna vitae risus. Nulla eleifend enim justo, id egestas neque pellentesque ac. Cras pellentesque aliquet est, eu interdum odio. Donec ultricies vel diam non vulputate.",
         e2: 1
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
