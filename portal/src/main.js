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

app.provide("URL_API_DISCIPLINAS", "api/club/disciplinas");
app.provide("URL_API_LICENCIA", "api/me/license");
app.provide("URL_API_CLUB", "api/club/info");
app.provide("URL_API_SOCIOS_DISCIPLINAS", "api/club/socios-disciplinas")
app.provide("URL_API_SOCIOS_GENERO", "api/club/socios-genero")
app.provide("URL_API_SOCIOS_AÑO", "api/club/socios-años")
app.provide("URL_API_PAYMENTS", "api/me/payments") // GET en ListadoCuotas, POST para pagar.
app.provide("URL_API_DEBT", "api/me/pending_payments")

app.use(createPinia());
app.use(router);
app.use(store);

app.mount("#app");
