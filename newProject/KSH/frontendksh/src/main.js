import App from "./App";
import store from "./store";
import { createApp } from "vue";

const app = createApp(App);
app.use(store);
app.mount("#app");
