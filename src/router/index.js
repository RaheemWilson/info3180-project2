import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '@/store/store.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/explore',
      name: 'explore',
      component: () => import('../views/ExploreView.vue'),
      meta: { requiresAuth: true }
    },
  ]
})

const redirectToLogin = route => {
  const login = 'login';
  if (route.name != login) {
    return { name: login, replace: true, query: { redirectFrom: route.fullPath } };
  }
};

router.beforeEach((to) => {
  let token = store.state.auth || localStorage.getItem("authToken")
  console.log(token)
  let userIsAuthenticated = token !== null
  const requiresAuth = to.matched.some((route) => route.meta && route.meta.requiresAuth);

  if (!userIsAuthenticated && requiresAuth) {
    return redirectToLogin(to);
  }

  return true;
});

export default router
