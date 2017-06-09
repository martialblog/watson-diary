import Home from './Home.vue';
import Logout from './Logout.vue';
import Diary from './Diary.vue';
import Usermanager from './Usermanager.vue';
import Reportmanager from './Reportmanager.vue';
import Feedmanager from './Feedmanager.vue';
import Diarymanager from './Diarymanager.vue';
import Profilemanager from './Profilemanager.vue';

export default [
  {path: '/', redirect: '/home' },
  {path: '/home', component: Home},
  {path: '/reportmanager', component: Reportmanager},
  {path: '/feedmanager', component: Feedmanager},
  {path: '/diarymanager', component: Diarymanager},
  {path: '/profilemanager', component: Profilemanager},
  {path: '/usermanager', component: Usermanager},
  {path: '/diary', component: Diary},
  {path: '/logout', component: Logout}
];
