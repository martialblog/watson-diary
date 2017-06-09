import Vue from 'vue';
import App from './App.vue';
import Vuetify from 'vuetify';
import VueRouter from 'vue-router';
import Routes from './routes.js';

Vue.use(VueRouter);
Vue.use(Vuetify);

const router = new VueRouter({
  routes: Routes
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router
});
