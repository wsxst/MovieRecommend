import Vue from 'vue'
import Router from 'vue-router'
import Index from './components/Index.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Login')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('./views/Register')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('./views/Profile')
    },
    {mode: 'hash',
      path: "/movie_info",
      name: "movie_info",
      component: () => import('./views/MovieInfo')
    },
  ],
    mode: 'hash',
    base: '/',
})
