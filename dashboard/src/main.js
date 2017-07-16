import Vue from 'vue';
import App from './App.vue';
import Vuetify from 'vuetify';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import Routes from './routes.js';

import Chart from './Chart.vue';
import LineChart from './LineChart.vue';

Vue.component('chart', Chart);
Vue.component('linechart', LineChart);

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router
});
