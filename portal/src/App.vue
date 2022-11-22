<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="wrapper">
      <div id="navbar">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container-fluid">
            <RouterLink class="navbar-brand" to="/"
              >Club Villa Elisa</RouterLink
            >
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNavDropdown"
              aria-controls="navbarNavDropdown"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNavDropdown">
              <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                  <RouterLink class="nav-link mx-2" aria-current="page" to="/"
                    >Home</RouterLink
                  >
                </li>
                <li class="nav-item">
<<<<<<< HEAD
                  <RouterLink
                    class="nav-link mx-2"
                    aria-current="page"
                    to="/auth"
                    >Login</RouterLink
                  >
                </li>
                <li class="nav-item">
                  <RouterLink
                    class="nav-link mx-2"
                    aria-current="page"
                    to="/disciplinas"
                    >Disciplinas</RouterLink
                  >
=======
                  <RouterLink class="nav-link mx-2" aria-current="page" to="/disciplinas">Disciplinas</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink class="nav-link mx-2" aria-current="page" to="/estadisticas">Estadisticas</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink class="nav-link mx-2" aria-current="page" to="/pagos">Pagos</RouterLink>
>>>>>>> b09bd8e9f4101cf6c0f7735bd51df0cf7ef89fbc
                </li>
              </ul>
              <ul v-if="estaLogueado" class="navbar-nav ms-auto d-lg-inline-flex">
                <li class="nav-item dropdown">
                  <a
                    class="nav-link mx-2 dropdown-toggle"
                    href="#"
                    id="navbarDropdownMenuLink"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    {{ authSocio.nombre }} {{ authSocio.apellido }}
                  </a>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="navbarDropdownMenuLink"
                  >
                    <li><a class="dropdown-item" href="#">Perfil</a></li>
                    <li><a class="dropdown-item" @click="logout">Cerrar Sesion</a></li>
                  </ul>
                </li>
              </ul>
              <ul v-else class="navbar-nav ms-auto d-lg-inline-flex">
                <li class="nav-item dropdown">
                  <RouterLink
                    class="nav-link mx-2"
                    aria-current="page"
                    to="/auth"
                    >Login</RouterLink
                  >
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters({
      authSocio: "auth/socio",
      estaLogueado: "auth/isLoggedIn",
    }),
  },

  methods: {
    ...mapActions("auth", ["logoutSocio"]),

    async logout() {
      await this.logoutSocio().catch((err) => {
        console.log(err);
      });
      this.error = false;
      this.socio = {
        email: null,
        password: null,
      };
      this.$router.push("/");
    },
  }
};
</script>