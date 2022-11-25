<template>
    <div class="card mb-3" style="max-width: 1080px;" v-if="socio">
        <div class="row no-gutters">
            <div class="col-md-3">
                <img src="" class="card-img" alt="...">
            </div>

            <div class="col-md-6">
                <div class="card-body">
                    <h5 class="card-title"> {{ socio.profile.email }}</h5>
                    <p class="card-text"> {{ socio.profile.address }}</p>
                    <p class="card-text"> {{ socio.profile.gender }}</p>
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
        let config = {
            headers: {
                id: 10,
            }
        }
        apiService
            .get("api/me/license", config)
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
  