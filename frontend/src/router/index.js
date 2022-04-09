import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';
import ApplySend from "@/views/ApplySend";
import UserCabinet from "@/views/UserCabinet";
import ChangeUserProfile from "@/views/ChangeUserProfile";
import ApplyDetails from "@/views/ApplyDetails";


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: AboutView
  },
  {
    path: '/apply_send',
    name: 'apply_send',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: ApplySend
  },
  {
    path: '/user_cabinet',
    name: 'user_cabinet',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: UserCabinet
  },
  {
    path: '/change_profile',
    name: 'change_profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: ChangeUserProfile
  },
  {
    path: '/apply_details',
    name: 'apply_details',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    component: ApplyDetails
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
