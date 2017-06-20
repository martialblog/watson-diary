import Home from './Home.vue';
import Help from './Help.vue';
import Diary from './Diary.vue';
import Usermanager from './Usermanager.vue';
import Reportmanager from './Reportmanager.vue';
import Feedmanager from './Feedmanager.vue';
import Profile from './Profile.vue';

export default [
  {path: '/', component: Home},
  {path: '/admin/reportmanager', component: Reportmanager},
  {path: '/admin/feedmanager', component: Feedmanager},
  {path: '/admin/usermanager', component: Usermanager},
  {path: '/profile/:username', component: Profile},
  {path: '/diary/:username', component: Diary},
  {path: '/help', component: Help}
];
