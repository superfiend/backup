import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'
import Words from "../components/Words";
import PlusWord from "../components/PlusWord";

Vue.use(Router);
Vue.use(Resource);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'words',
      component: Words
    },
    {
      path: '/word/plus',
      name: 'plusword',
      component: PlusWord
    }
  ],
  mode: 'history'
})
