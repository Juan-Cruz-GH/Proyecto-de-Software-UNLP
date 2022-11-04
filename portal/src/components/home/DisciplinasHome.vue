<template>
  <div class="row" v-if="disciplines && disciplines.length">
    <div class="col-sm-9 col-md-7 col-lg-6 mx-auto">
      <div class="card border-0 shadow rounded-3 my-5">
        <div class="card-body p-4 p-sm-5">
          <h5 class="card-title text-center mb-5 fw-light fs-5">Disciplinas</h5>
          <div v-for="i in Array(rows).keys()"
            :key="i">
            <div class="row mb-3">
              <div v-for="(discipline, index) in disciplines_row[i]" 
                  :key="index" 
                  class="col-sm-9 col-md-7 col-lg-6">
                <div class="card text-center">
                <div class="card-header"></div>
                <div class="card-body">
                  <h5 class="card-title">{{discipline.name}}</h5>
                  <p class="card-text">
                    <ul class="list-group">
                      <li class="list-group-item"><strong>Profesores: </strong>{{discipline.teacher}}</li>
                      <li class="list-group-item"><strong>Horarios: </strong>{{discipline.time}}</li>
                      <li class="list-group-item"><strong>Categoria: </strong>{{discipline.category}}</li>
                      <li class="list-group-item"><strong>Dias: </strong>{{discipline.days}}</li>
                      <li class="list-group-item"><strong>Costo: </strong>{{discipline.price}}</li>
                    </ul>
                  </p>
                </div>
                <div class="card-footer text-muted"></div>
              </div>
            </div>
          </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      disciplines: [],
      disciplines_row: [],
      errors: [],
      rows: 0,
    };
  },
  // Fetches posts when the component is created.
  created() {
    axios
      .get("http://127.0.0.1:5000/api/club/disciplinas")
      .then((response) => {
        // JSON responses are automatically parsed.
        this.disciplines = response.data;
        this.rows = this.disciplines.length % 2 == 0 ? this.disciplines.length / 2 : Math.floor((this.disciplines.length / 2) + 1);
        this.disciplines.forEach((value, index) => {
          if ((index != 0) && (index % 2 != 0)) {
            return;
          }
          this.disciplines_row.push(this.disciplines.slice(index, index+2))
        });
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
