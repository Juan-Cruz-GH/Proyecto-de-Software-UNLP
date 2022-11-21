import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import store from "./store"

//import "./assets/main.css";

const app = createApp(App);

const header = "https://admin-grupo23.proyecto2022.linti.unlp.edu.ar";
// https://admin-grupo23.proyecto2022.linti.unlp.edu.ar     cambiar header a este antes de cada push/merge a main
// http://127.0.0.1:5000                                    cambiar header a este para correr la app localmente

app.provide("URL_API_DISCIPLINAS", header + "/api/club/disciplinas");
app.provide("URL_API_LICENCIA", header + "/api/me/license");
app.provide("URL_API_CLUB", header + "/api/club/info");
app.provide("URL_API_SOCIOS_DISCIPLINAS", header + "/api/club/socios-disciplinas")
app.provide("URL_API_SOCIOS_GENERO", header + "/api/club/socios-genero")
app.provide("URL_API_SOCIOS_AÑO", header + "/api/club/socios-años")
app.provide("URL_API_PAYMENTS", header + "/api/me/payments") // GET en ListadoCuotas, POST para pagar.

app.use(createPinia());
app.use(router);
app.use(store);

app.mount("#app");
