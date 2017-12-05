import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueRouter from 'vue-router'
import Octicon from 'vue-octicon/components/Octicon.vue'
import 'vue-octicon/icons'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(VueRouter)
Vue.component('octicon', Octicon)

import App from './App.vue'
import ReportContainer from './containers/ReportContainer.vue'
import UnitemizedItemsContainer from './containers/UnitemizedItemsContainer.vue'
import MonetaryContributionsContainer from './containers/MonetaryContributionsContainer.vue'
import InKindContributionsContainer from './containers/InKindContributionsContainer.vue'

import store from './store'
console.log(store)
const routes = [
  {
    path: '/reports/:id', component: ReportContainer, // TODO: slug instead of id?
    children: [
      {
        path: 'unitemized-items',
        component: UnitemizedItemsContainer
      },
      {
        path: 'monetary-contributions',
        component: MonetaryContributionsContainer
      },
      {
        path: 'in-kind-contributions',
        component: InKindContributionsContainer
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
});
