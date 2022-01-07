import { createApp } from 'vue'
import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import About from './About.vue'

const routes = [
  { path: '/', component: App },
  { path: '/about', component: About },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes, 
})


const app = createApp({})
app.use(router)
app.mount('#app')
