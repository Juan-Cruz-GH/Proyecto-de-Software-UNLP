<template>
    <table id="tableComponent" class="table table-bordered table-hover">
        <thead>
            <tr>
                <!-- Listar los campos para la tabla -->
                <th style="text-align: center" v-for="campo in campos">
                    {{ campo }}
                </th>
            </tr>
        </thead>
        <tbody>
            <!-- Listar data de cada fila, si la llave es precio le agrego el signo $ -->
            <tr v-for="item in disciplines" :key='item'>
                <td style="text-align: center" v-for="key in keys" :key='key'>
                    <span v-if="esPrecio(key)">$ {{ item[key] }}</span>
                    <span v-else>{{ item[key] }}</span>
                </td>
            </tr>
        </tbody>
    </table>
    <div id="pre-footer" style="min-height: 40vh;">
    </div>
</template>
  
<script>
export default {
    inject: ['URL_API_DISCIPLINAS'],
    data() {
        return {
            disciplines: [],
            errors: [],
            campos: ["Nombre", "Categoria", "Dias", "Horario", "Profesor", "Precio"],
            keys: ["name", "category", "days", "time", "teacher", "price"],
        };
    },
    methods: {
        esPrecio(key) {
            return (key === "price")
        }
    },
    computed: {
    },
    // Fetches posts when the component is created.
    created() {
        axios
            .get(this.URL_API_DISCIPLINAS)
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
  