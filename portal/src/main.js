import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

//import "./assets/main.css";

const app = createApp(App);

const headerLocal = "http://127.0.0.1:5000/api";
const headerRemoto = "https://admin-grupo23.proyecto2022.linti.unlp.edu.ar/api";

app.provide("URL_API_DISCIPLINAS", headerLocal + "/club/disciplinas");
app.provide("URL_API_LICENCIA", headerLocal + "/me/license");
app.provide("URL_API_CLUB", headerLocal + "/club/info");
// cambiar headerLocal por headerRemoto en los provides antes de push a main

app.use(createPinia());
app.use(router);

app.mount("#app");
