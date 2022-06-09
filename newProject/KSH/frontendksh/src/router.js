import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "./components/HomePage";
import NotFound from "./components/404Page";
import AutorizePage from "./components/AutorizePage";
import LoadFile from "./components/LoadFile";
import CardsPage from "./components/CardsPage";
import ContesterPage from "./components/ContesterPage";
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
    { path: "/generate/excel", component: LoadFile },
    { path: "/generate/contester", component: ContesterPage },
    { path: "/groups", component: CardsPage },
  ],
});
