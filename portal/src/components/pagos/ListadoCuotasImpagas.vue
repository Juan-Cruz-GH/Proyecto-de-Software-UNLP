<template>
    <h1 style="text-align:center">
        <strong>Cuotas adeudadas</strong>
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
            <tr style="text-align: center;" v-for="cuotaImpaga, i in dataPagina">
                <td>$ {{ cuotaImpaga.amount }}</td>
                <td>{{ cuotaImpaga.month }}</td>
                <td>{{ cuotaImpaga.year }}</td>
                <td>
                    <input id="{{cuotaImpaga.month}}" type="file" @change="seSubioComprobante">
                    <button>Pagar</button>
                    <!-- <button class="btn btn-primary" type="button">Subir comprobante</button>-->
                </td>
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
</template>
  
<script>
import { apiService } from "@/api";

export default {
    data() {
        return {
            cuotasImpagas: [],
            errors: [],
            campos: ["Total", "Mes de cuota", "Año", "Pagar (subir comprobante .pdf / .png / .jpg)"],
            porPagina: 5,
            dataPagina: [],
            paginaActual: 1,
            comprobantes: [],
            i: 0
        };
    },
    methods: {
        seSubioComprobante(event) {
            console.log("evento ", event)
            console.log((document.getElementById("5").value).split("\\")[2])
            this.comprobantes[this.i] = event.target.files[this.i];
        },
        comprobanteEsValido() {
            return (this.comprobantes[this.i].name.includes("jpg")
                || this.comprobantes[this.i].name.includes("pdf")
                || this.comprobantes[this.i].name.includes("png"))
        },
        pagar(cuotaImpaga) {
            if (this.comprobanteEsValido) {
                function getCookie(name) {
                    const value = `; ${document.cookie}`;
                    const parts = value.split(`; ${name}=`);
                    if (parts.length === 2) return parts.pop().split(';').shift();
                }
                let archivo = comprobante.target.files[0];
                if (archivo.name.includes("jpg") || archivo.name.includes("pdf") || archivo.name.includes("png")) {
                    this.comprobante = comprobante;
                }
                console.log(this.comprobante)
                const options = {
                    credentials: 'same-origin',
                    headers: {
                        'X-CSRF-TOKEN': getCookie('csrf_access_token'),
                    },
                };
                apiService
                    .post("/api/me/payments", options)
                    .then(() => {
                        window.location.reload();
                        this.getDataPagina(1);
                    })
                    .catch((e) => {
                        this.errors.push(e);
                    });
            }
        },
        getTotalPaginas() {    // Redondeo por si da con decimales
            return Math.ceil(this.cuotasImpagas.length / this.porPagina);
        },
        getDataPagina(numPagina) {
            this.paginaActual = numPagina;
            this.dataPagina = [];
            let inicio = (numPagina * this.porPagina) - this.porPagina;
            let fin = (numPagina * this.porPagina);
            this.dataPagina = this.cuotasImpagas.slice(inicio, fin);
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
        apiService
            .get("/api/me/pending_payments")
            .then((response) => {
                this.cuotasImpagas = response.data;
                this.getDataPagina(1);
            })
            .catch((e) => {
                this.errors.push(e);
            });
    },
};
</script>
  