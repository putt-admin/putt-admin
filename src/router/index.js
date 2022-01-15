import { createWebHistory, createRouter } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Login from "../views/Login.vue";
import Builder from "../views/Builder.vue";
import BuilderPages from '../components/BuilderPages.vue';
import BuilderDesignPage from '../components/BuilderDesignPage.vue';

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/builder",
    name: "Builder",
    component: Builder,
    children: [
      { path: '', component: BuilderPages },
      { path: 'default/page/:pageName', component: BuilderDesignPage },
    ]
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;