<template>
  <div>
    <v-parallax src="/public/hero_bg.png">
      <v-layout column align-center justify-center>
        <v-flex xs12>
          <h1 class="white--text">{{headline}}</h1>
          <h4 class="white--text">{{subheader}}</h4>
        </v-flex>
        <v-flex xs12 class="text-xs-center mt-2" style="width:700px;">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget efficitur massa. Ut aliquet sodales nibh quis consectetur. Fusce in sollicitudin neque. Maecenas sagittis purus turpis, nec dapibus elit congue non. Praesent volutpat neque ut magna luctus vehicula. Proin dignissim lorem et finibus malesuada. Sed justo sapien, volutpat sed sagittis sollicitudin, ultrices eget nibh. Aenean quam ante, lobortis et faucibus ut, sagittis eu turpis. Integer efficitur, lectus sed maximus consectetur, magna ante blandit mi, sit amet sodales ante ipsum quis nisi. Vivamus tincidunt leo eu pretium ultricies. Nunc lobortis dui est, ac ullamcorper eros iaculis quis.</p>
        </v-flex>
      </v-layout>
    </v-parallax>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        headline: "Dr. Watson",
        subheader: "Lorem ipsum dolor sit amet",
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
