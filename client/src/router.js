import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import OneOne from '@/components/pages/OneOne'



Vue.use(Router)

export default new Router({

  routes: [
    {
      path: '/',
      name: 'OneOne',
      component: OneOne
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    }
  ]
})