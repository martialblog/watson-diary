import Admin from './Admin.vue';
import Welcome from './Welcome.vue';
import Profile from './Profile.vue';
import Logout from './Logout.vue';
import Report from './Report.vue';

export default [
  {path: '/', redirect: '/home' },
  {path: '/home', component: Welcome},
  {path: '/admin', component: Admin},
  {path: '/profile', component: Profile},
  {path: '/report', component: Report},
  {path: '/logout', component: Logout}
];
