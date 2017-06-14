<template>
  <v-app>
    <v-navigation-drawer
      class="pb-0"
      height="100%"
      persistent
      dark
      :mini-variant.sync="mini"
      v-model="drawer"
    >
      <v-list dense>
        <template v-for="(item, i) in items">
          <v-layout
            row
            v-if="item.heading"
            align-center
            :key="i"
          >
            <v-flex xs6>
              <v-subheader v-if="item.heading">
                {{ item.heading }}
              </v-subheader>
            </v-flex>
          </v-layout>
          <v-list-group v-else-if="item.children" v-model="item.model" no-action>
            <v-list-item slot="item">
              <v-list-tile>
                <v-list-tile-action>
                  <v-icon>{{ item.model ? item.icon : item['icon-alt'] }}</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title>
                    {{ item.text }}
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list-item>
            <v-list-item
              v-for="(child, i) in item.children"
              :key="i"
            >
              <v-list-tile router :to="child.link">
                <v-list-tile-action v-if="child.icon">
                  <v-icon>{{ child.icon }}</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title>
                    {{ child.text }}
                  </v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else>
            <v-list-tile router :to="item.link">
              <v-list-tile-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>
                  {{ item.text }}
                </v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list-item>
        </template>
      </v-list>
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
    data: () => ({
      drawer: true,
      mini: false,
      items: [
        { icon: 'dashboard', text: 'Home', link: '/home' },
        {
          icon: 'account_circle',
          'icon-alt': 'keyboard_arrow_down',
          text: 'Profile' ,
          model: false,
          children: [
            { text: 'Diary', link: '/diary' },
            { text: 'Manage Profile', link: '/profilemanager' },
          ]
        },
        {
          icon: 'build',
          'icon-alt': 'keyboard_arrow_down',
          text: 'Admin',
          model: false,
          children: [
            { text: 'Users', link: '/usermanager'},
            { text: 'Reports', link: '/reportmanager'},
            { text: 'Feeds', link: '/feedmanager'},

          ]
        },
        { icon: 'help', text: 'Help', link: '/help' },
        { icon: 'chat_bubble', text: 'Send feedback', link: '/feedback'},
      ]
    })
  }
</script>


<style lang="stylus">
  @import './stylus/main'
</style>
