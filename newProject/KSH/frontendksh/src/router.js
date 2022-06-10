import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "./components/HomePage";
import NotFound from "./components/404Page";
import AutorizePage from "./components/AutorizePage";
import LoadFile from "./components/LoadFile";
import CardsPage from "./components/CardsPage";
import Register from "./components/Register";
import ContesterPage from "./components/ContesterPage";
import AutorizedHomePage from "./components/AutorizedHomePage";
export default createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes: [
    {
      path: "/:catchAll(.*)",
      name: "NotFound",
      component: NotFound,
    },
    { path: "/", component: HomePage },
    { path: "/home", component: AutorizedHomePage },
    { path: "/signin", component: AutorizePage },
    { path: "/signin", component: AutorizePage },
    { path: "/generate/excel", component: LoadFile },
    { path: "/generate/contester", component: ContesterPage },
    { path: "/groups", component: CardsPage },
    { path: "/register", component: Register },
  ],
});
