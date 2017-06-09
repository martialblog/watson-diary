<template>
  <v-container fluid>
    <v-card>
      <v-card-text class="mt-3">
        <div>{{ text }}</div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In cursus sapien dui, at sollicitudin felis pellentesque vel. Curabitur lobortis, nibh ut aliquam malesuada, ante nisi lobortis purus, sed egestas justo urna vitae risus. Nulla eleifend enim justo, id egestas neque pellentesque ac. Cras pellentesque aliquet est, eu interdum odio. Donec ultricies vel diam non vulputate. Sed justo metus, interdum ut enim ut, pharetra viverra nulla. Aenean sed orci diam. Vivamus et arcu luctus, lacinia nulla nec, consequat arcu. Integer convallis ex justo, vel elementum purus elementum a. Suspendisse varius ipsum eget mi blandit, vitae efficitur ligula efficitur. Proin ante nibh, dictum non nulla quis, hendrerit tincidunt lectus. Vestibulum porta justo elit, at luctus ex tempus quis.",
      }
    }
  }
</script>

<style lang="stylus">
  @import './stylus/main'
</style>
