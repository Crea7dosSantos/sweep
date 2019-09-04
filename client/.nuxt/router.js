import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _d2a54216 = () => interopDefault(import('../pages/signin.vue' /* webpackChunkName: "pages/signin" */))
const _a978952a = () => interopDefault(import('../pages/signup.vue' /* webpackChunkName: "pages/signup" */))
const _9571bd62 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
      path: "/signin",
      component: _d2a54216,
      name: "signin"
    }, {
      path: "/signup",
      component: _a978952a,
      name: "signup"
    }, {
      path: "/",
      component: _9571bd62,
      name: "index"
    }],

  fallback: false
}

export function createRouter() {
  return new Router(routerOptions)
}
