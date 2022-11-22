import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import DisciplinasView from "../views/DisciplinasView.vue";
import LoginView from "../views/LoginView.vue";
import EstadisticasView from "../views/EstadisticasView.vue";
import PagosView from "../views/PagosView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/disciplinas",
      name: "disciplinas",
      component: DisciplinasView,
    },
    {
      path: "/auth",
      name: "auth",
      component: LoginView,
    },
    {
      path: "/pagos",
      name: "pagos",
      component: PagosView,
    },
    {
      path: "/estadisticas",
      name: "estadisticas",
      component: EstadisticasView,
    }
  ],
});

export default router;
