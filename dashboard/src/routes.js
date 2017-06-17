import Home from './Home.vue';
import Logout from './Logout.vue';
import Diary from './Diary.vue';
import Usermanager from './Usermanager.vue';
import Reportmanager from './Reportmanager.vue';
import Feedmanager from './Feedmanager.vue';
import Profilemanager from './Profilemanager.vue';

export default [
  {path: '/', component: Home},
  {path: '/admin/reportmanager', component: Reportmanager},
  {path: '/admin/feedmanager', component: Feedmanager},
  {path: '/admin/usermanager', component: Usermanager},
  {path: '/profilemanager/:username', component: Profilemanager},
  {path: '/diary', component: Diary},
  {path: '/logout', component: Logout}
];
