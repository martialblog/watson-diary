<template>
  <v-app>
    <v-navigation-drawer  persistent dark :mini-variant.sync="mini" v-model="drawer">
      <v-card class="ma-4">
        <v-list dense class="py-0">
          <v-list-item v-for="item in items" :key="item">
            <router-link :to="item.link" style="text-decoration:none;">
              <v-list-tile>
                <v-list-tile-action>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </router-link>
          </v-list-item>
        </v-list>
      </v-card>
    </v-navigation-drawer>

    <v-toolbar class="blue accent-4" light>
      <v-toolbar-side-icon light @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Dr. Watson Dashboard</v-toolbar-title>
    </v-toolbar>
    <main>
      <router-view></router-view>
    </main>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        drawer: true,
        items: [
          { title: 'Home', icon: 'dashboard', link: '/home'},
          { title: 'Admin', icon: 'build', link: '/admin'},
          { title: 'Profile', icon: 'account_circle', link: '/profile'},
          { title: 'Logout', icon: 'exit_to_app', link: '/logout'}

        ],
        right: null,
      }
    }
  }
</script>


<style lang="stylus">
  @import './stylus/main'
</style>
