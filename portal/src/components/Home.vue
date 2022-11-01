<script setup>
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
</script>

<template>
  <div>
    <h1>Disciplinas:</h1>
    <ul v-if="disciplinas && disciplinas.length">
      <li v-for="(disciplina, index) in disciplinas" :key="index">
        <strong>{{ index }}</strong> - {{ disciplina.name }} - {{disciplina.days}} - {{disciplina.time}}
      </li>
    </ul>
    <ul v-if="errors && errors.length">
      <li v-for="(error, index) in errors" :key="index">
        {{ error.message }}
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  data() {
    return {
      disciplinas: [],
      errors: [],
    };
  },
  // Fetches posts when the component is created.
  created() {
    axios
      .get("http://127.0.0.1:5000/api/club/disciplinas")
      .then((response) => {
        // JSON responses are automatically parsed.
        this.disciplinas = response.data
      })
      .catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>
