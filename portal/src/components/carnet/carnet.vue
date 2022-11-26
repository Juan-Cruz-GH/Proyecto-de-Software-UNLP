<template>
    <div id="carnet" class="container" style="font-family:'Comic Sans MS','Comic Sans',cursive;width: 600px; min-height: 80vh; "
        v-if="socio">
        <br>
        <div class="card border-dark border border-5 text-center" style="width: 600px;">
            <div class="row">
                <div class="column-12">
                    <h1 style="font-family:'Brush Script MT', cursive; font-size:4rem; border-bottom:5px solid;">
                        Club Deportivo
                        Villa
                        Elisa</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-7">
                    <div class="card-body">
                        <span style="font-size: 1.5rem ;">{{ socio.profile.apellido }} {{ socio.nombre }}</span><br>
                        {{ socio.tipo_documento }}: {{ socio.dni }} <br>
                        Socio: #{{ socio.id }} <br>
                        Email: {{ socio.email }}<br>
                        Género: {{ socio.gender }}
                        Dirección: {{ socio.address }}
                        Teléfono: {{ socio.phone }}
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <img src="" class="card-img" alt="...">
        </div>
        <p v-if="socio">
            {{ socio.profile.email }}
        </p>
    </div>
</template>
  
<script>
import { apiService } from "@/api";

export default {
    inject: ['URL_API_LICENCIA'],
    data() {
        return {
            socio: '',
            errors: [],
        };
    },
    // Fetches posts when the component is created.
    created() {
        apiService
            .get("api/me/license")
            .then((response) => {
                // JSON responses are automatically parsed.
                this.socio = response.data;
            })
            .catch((e) => {
                this.errors.push(e);
            });
    },
};
</script>
  