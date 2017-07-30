<template>
  <div>
    <v-parallax src="/public/hero_bg.png" class="">
      <v-layout column align-center justify-center>
        <v-flex xs12 class="text-xs-center">
          <h1 class="white--text">{{title}}</h1>
          <h4 class="white--text">{{subtitle}}</h4>
        </v-flex>
      </v-layout>
        <v-layout column align-center justify-center>
          <v-flex xs3 class="text-xs-center mt-2"></v-flex>
          <v-flex xs6 class="text-xs-center mt-2">
          <p>
            Dr. Watson offers an automatic Emotion and Personality analization tool, that aggregates your Social Media Stream and provides insight into emotional, social, and language tones. You can use these results to improve the perception and effectiveness of your communications, ensuring that your writing conveys the tone and style that you want for your intended audience.
          </p>
          </v-flex>
          <v-flex xs3 class="text-xs-center mt-2"></v-flex>
        </v-layout>

        <v-layout column align-center justify-center>
          <div class="text-xs-center">
            <v-btn round primary light router to="/help">More Info</v-btn>
          </div>
        </v-layout>

    </v-parallax>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        title: "Dr. Watson",
        subtitle: "Emotion and Personality Analization with IBM Watson"
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
