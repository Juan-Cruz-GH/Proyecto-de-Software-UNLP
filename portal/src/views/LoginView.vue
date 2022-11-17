<template>
  <header>
    <div id="navbar">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="/">Club Villa Elisa</RouterLink>
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
        </div>
      </nav>
    </div>
  </header>
  <div v-if="isLoggedIn">
    <h3>Usuario: {{ authSocio.name }}</h3>
    <h3>Mail: {{ authSocio.email }}</h3>
    <h3>Id: {{ authSocio.id }}</h3>

    <button type="button" @click="logout">Logout</button>
  </div>
  <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
    <div class="card border-0 shadow rounded-3 my-5">
      <div class="card-body p-4 p-sm-5">
        <h5 class="card-title text-center mb-5 fw-light fs-5">Log In</h5>
        <form action class="form" @submit.prevent="login">
          <div class="mb-3">
            <label class="form-label" for="#socio.email">Email</label>
            <input
              class="form-control"
              type="email"
              name="email"
              placeholder="Correo"
              v-model="socio.email"
              id="email"
              required
            />
          </div>
          <div class="mb-3">
            <label class="form-label" for="#socio.password">Password</label>
            <input
              class="form-control"
              type="password"
              name="password"
              placeholder="Clave"
              v-model="socio.password"
              id="password"
              required
            />
          </div>
          <input
            class="btn btn-primary btn-login text-uppercase fw-bold"
            type="submit"
            value="Login"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "LoginView",
  data: () => ({
    error: false,
    socio: {
      email: null,
      password: null,
    },
  }),

  computed: {
    ...mapGetters({
      authSocio: "auth/socio",
      isLoggedIn: "auth/isLoggedIn",
    }),
  },

  methods: {
    ...mapActions("auth", ["loginSocio", "logoutSocio"]),

    async login() {
      await this.loginSocio(this.socio).catch(() => {
        this.error = true;
      });
      this.socio = {
        email: null,
        password: null,
      };

      if (this.isLoggedIn) {
        this.$router.push("/");
      }
    },

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
  },
};
</script>
