<template>
    <br>
    <div id="carnet" class="container" style="font-family:'Comic Sans MS','Comic Sans',cursive;width: 600px;"
        v-if="socio">
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
                <div class="col-5">
                    <img class="card-img-left" src="{{photo}}" width="240rem" style="border-radius:50%" ;>
                </div>
                <div class="col-7">
                    <div class="card-body">
                        <span style="font-size: 1.5rem ;">{{ socio.profile.apellido }} {{ socio.nombre }}</span><br>
                        {{ socio.tipo_documento }}: {{ socio.dni }} <br>
                        Socio: #{{ socio.id }} <br>
                        Fecha alta: {{ socio.inserted_at.strftime('%Y-%m-%d') }}<br>
                    </div>
                </div>
            </div>
            <div class=" row">
                <div class="col-5" style="font-size: 2rem; ">
                    <br> Estado:<br>{%if socio.activo%} Activo{%else%} Inactivo{%endif%}
                </div>
                <div class="col-7">
                    <img class="card-img-left" src="{{}}" width="200rem">
                </div>
            </div>
            <br>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            socio: '',
            errors: [],
        };
    },
    // Fetches posts when the component is created.
    created() {
        let config = {
            headers: {
                id: 10,
            }
        }
        axios
            .get("http://127.0.0.1:5000/api/me/license", config)
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
  