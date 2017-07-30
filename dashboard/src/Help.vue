<template>
  <v-container fluid>

    <v-card>
      <v-card-text>
        <h4>Help</h4>
        <div><p>
The IBM Watson™ Tone Analyzer service is based on the theory of psycholinguistics, a field of research that explores the relationship between linguistic behavior and psychological theories. The service uses linguistic analysis and the correlation between the linguistic features of written text and emotional, social, and language tones to develop scores for each of these tone dimensions.</p>

<p>Psycholinguistics researchers have worked to understand whether the words that we use in our day-to-day lives reflect who we are, how we feel, and how we think. After several decades of research in this area, it is now accepted in psychology, marketing, and other fields that language reflects more than just what we want to say. The frequency with which we use certain types of words can provide clues to personality, thinking style, social connections, and emotional states.</p>
        </div>
      </v-card-text>
    </v-card>

    <v-card class="blue darken-1 white--text mt-3">
      <v-card-text>
        <h4 class="white--text">Usage</h4>
        <div class="white--text">

          <h6 class="white--text">Users</h6>
          <p>The Usermanagement offers the possibility to view/modify current Users and add new ones.</p>
          <h6 class="white--text">Reports</h6>
          <p>The Reportmanager lets you view/delete the generated Reports for all Users.</p>
          <h6 class="white--text">Feeds</h6>
          <p>The Feedmanager lets you add new Feeds for your Users.</p>

        </div>
      </v-card-text>
    </v-card>

</v-container>
</template>

<script>
  import Lorem from 'lorem-ipsum';

  export default {
    data () {
      return {
        text: ""
      }
    },
    created () {
      this.text = Lorem({
        count: 30
      })

    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
