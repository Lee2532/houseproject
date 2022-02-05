import Vue from 'vue';
import VueRouter from 'vue-router';

import store from '@/store';

import Dashboard from '@/views/Dashboard';
import Home from '@/views/Home.vue';
import Product from '@/views/Product.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {requiresAuth: true},
  },
  {
    path: '/Product',
    name: 'Product',
    component: Product,
    props: true,
  },
  {
    path: '/productions/:id',
    name: 'productions',
    component: Product,
    props: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
