import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "./components/HomePage";
import NotFound from "./components/404Page";
import AutorizePage from "./components/AutorizePage";
export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/:catchAll(.*)",
      name: "NotFound",
      component: NotFound,
    },
    { path: "/home", component: HomePage },
    { path: "/signin", component: AutorizePage },
  ],
});
