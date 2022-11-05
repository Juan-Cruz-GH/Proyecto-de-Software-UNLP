<template>
    <table id="tableComponent" class="table table-bordered table-striped">
        <thead>
            <tr>
                <!-- Listar los campos para la tabla -->
                <th v-for="campo in campos">
                    {{ campo }} <i class="bi bi-sort-alpha-down" aria-label='Sort Icon'></i>
                </th>
            </tr>
        </thead>
        <tbody>
            <!-- Listar data de cada fila -->
            <tr v-for="item in disciplines" :key='item'>
                <td v-for="key in keys" :key='key'>
                    {{ item[key] }}
                </td>
            </tr>
        </tbody>
    </table>
</template>
  
<script>
export default {
    data() {
        return {
            disciplines: [],
            errors: [],
            campos: ["Nombre", "Categoria", "Dias", "Horario", "Profesor", "Precio"],
            keys: ["name", "category", "days", "time", "teacher", "price"],
        };
    },
    computed: {
        filterList() {
            return this.disciplines.filter(discipline => {
                return discipline.name.toLowerCase().includes(this.search.toLowerCase())
            })
        }
    },
    // Fetches posts when the component is created.
    created() {
        axios
            .get("http://127.0.0.1:5000/api/club/disciplinas")
            .then((response) => {
                // JSON responses are automatically parsed.
                this.disciplines = response.data;
            })
            .catch((e) => {
                this.errors.push(e);
            });
    },
};
</script>
  