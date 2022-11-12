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

  <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
    <div class="card border-0 shadow rounded-3 my-5">
      <div class="card-body p-4 p-sm-5">
        <h5 class="card-title text-center mb-5 fw-light fs-5">Log In</h5>
        <form method="POST">
          <div class="mb-3">
            <label class="form-label">Email</label>
            <input
              class="form-control"
              type="email"
              name="username"
              placeholder="Correo"
              v-model="username"
              required
            />
          </div>
          <div class="mb-3">
            <label class="form-label">Password</label>
            <input
              class="form-control"
              type="password"
              name="password"
              placeholder="Clave"
              v-model="password"
              required
            />
          </div>
          <input
            v-on:click="infoSocio"
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
export default {
  data() {
    return {
        username = '',
        password = '',
        mensaje = '',
        token = '',
    };
  },
  methods: {
    async infoSocio() {
        let socio = {
            username: this.username,
            password: this.password
        };
        let response = await axios.post("http://127.0.0.1:5000/api/auth", socio);
        this.mensaje = response.mensaje;
        this.token = response.token
    }
  },
};
</script>
