import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Accounts from '@/components/Accounts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/accounts',
      name: 'Accounts',
      component: Accounts
    }
  ]
})
