import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'
import Users from "../components/user/Users";
import AddUser from "../components/user/AddUser";

Vue.use(Router);
Vue.use(Resource);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Users',
      component: Users
    },
    {
      path: '/user/add',
      name: 'adduser',
      component: AddUser
    }
  ],
  mode: 'history'
})
