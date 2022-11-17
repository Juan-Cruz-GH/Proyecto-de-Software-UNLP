import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import DisciplinasView from "../views/DisciplinasView.vue";
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
      path: "/estadisticas",
      name: "estadisticas",
      component: EstadisticasView,
    },
    {
      path: "/pagos",
      name: "pagos",
      component: PagosView,
    }
  ],
});

export default router;
