import App from "./App.vue";
import router from "./router";
import { createApp } from "vue";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import axios from "axios";

const app = createApp(App);
app.config.productionTip = false;
app.use(store).use(router, axios, Antd);
app.mount("#app");
