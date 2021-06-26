import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store/index'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/SpreadSheet')
  },
  {
    path: '/spreadsheet',
    name: 'spreadsheet',
    component: () => import('../views/SpreadSheet'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login'),
    meta: {
      requiresGuest: true
    }
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register'),
    meta: {
      requiresGuest: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters['auth/authorized']) {
      next({
        name: 'login'
      })
    }
  }

  if (to.matched.some(record => record.meta.requiresGuest)) {
    if (store.getters['auth/authorized']) {
      next({
        name: 'spreadsheet'
      })
    }
  }

  next()
})

export default router
