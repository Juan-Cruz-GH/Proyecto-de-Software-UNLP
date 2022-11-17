<template>
    <h1 style="text-align:center">
        <strong>Cuotas pagas</strong>
    </h1>
    <div id="espacio" style="min-height: 2.5vh;">
    </div>
    <table id="tableComponent" class="table table-bordered table-hover">
        <thead>
            <tr>
                <th style="text-align: center" v-for="campo in campos">
                    <!-- Listar los campos para la tabla -->
                    {{ campo }}
                </th>
            </tr>
        </thead>
        <tbody>
            <tr style="text-align: center;" v-for="cuotaPaga in dataPagina">
                <td>$ {{ cuotaPaga }}</td>
                <td>{{ cuotaPaga }}</td>
                <td>{{ cuotaPaga }}</td>
                <td>{{ cuotaPaga }}</td>
            </tr>
        </tbody>
    </table>
    <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
            <li class="page-item" v-on:click="getPaginaAnterior()"><a class="page-link" href="#">Anterior</a></li>
            <li v-for="pagina in getTotalPaginas()" v-on:click="getDataPagina(pagina)" class="page-item"
                v-bind:class="estaActiva(pagina)">
                <a class="page-link" href="#"> {{ pagina }} </a>
            </li>
            <li class="page-item" v-on:click="getPaginaSiguiente()"> <a class="page-link" href="#">Siguiente</a></li>
        </ul>
    </nav>
    <div id="espacio" style="min-height: 30.5vh;"></div>
</template>
  
<script>
export default {
    inject: ['URL_API_PAYMENTS'],
    data() {
        return {
            cuotasPagas: [],
            errors: [],
            campos: ["Total", "Mes de cuota", "Fecha de pago", "Recibo"],
            porPagina: 5,
            dataPagina: [],
            paginaActual: 1
        };
    },
    methods: {
        getTotalPaginas() {    // Redondeo por si da con decimales
            return Math.ceil(this.cuotasPagas.length / this.porPagina);
        },
        getDataPagina(numPagina) {
            this.paginaActual = numPagina;
            this.dataPagina = [];
            let inicio = (numPagina * this.porPagina) - this.porPagina;
            let fin = (numPagina * this.porPagina);
            this.dataPagina = this.cuotasPagas.slice(inicio, fin);
        },
        getPaginaSiguiente() {
            if (this.paginaActual < this.getTotalPaginas()) {
                this.paginaActual++;
            }
            this.getDataPagina(this.paginaActual);
        },
        getPaginaAnterior() {
            if (this.paginaActual > 1) {
                this.paginaActual--;
            }
            this.getDataPagina(this.paginaActual);
        },
        estaActiva(numPagina) {
            return numPagina == this.paginaActual ? "active" : "";
        }
    },
    computed: {
    },
    created() {
        axios
            .get('URL_API_PAYMENTS')
            .then((response) => {
                this.cuotasPagas = response.data;
                this.getDataPagina(1);
            })
            .catch((e) => {
                this.errors.push(e);
            });
    },
};
</script>
  