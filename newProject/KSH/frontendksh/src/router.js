import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "./components/HomePage";
import NotFound from "./components/404Page";
import AutorizePage from "./components/AutorizePage";
import GenerateGroups from "./components/GenerateGroups";
export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/:catchAll(.*)",
      name: "NotFound",
      component: NotFound,
    },
    { path: "/", component: HomePage },
    { path: "/signin", component: AutorizePage },
    { path: "/generate", component: GenerateGroups },
    { path: "/generate/excel", component: GenerateGroups },
  ],
});
