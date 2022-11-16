import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

//import "./assets/main.css";

const app = createApp(App);

const header = "http://127.0.0.1:5000";
// https://admin-grupo23.proyecto2022.linti.unlp.edu.ar     header remoto
// http://127.0.0.1:5000                                    header local

app.provide("URL_API_DISCIPLINAS", header + "/api/club/disciplinas");
app.provide("URL_API_LICENCIA", header + "/api/me/license");
app.provide("URL_API_CLUB", header + "/api/club/info");
app.provide("URL_SOCIOS_GENERO", header + "api/club/socios-genero")

app.use(createPinia());
app.use(router);

app.mount("#app");
