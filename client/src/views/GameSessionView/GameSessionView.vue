<script setup>
import { ref } from "vue";
import axios from "axios";

const session = ref(() => {
  const response = axios.get('http://localhost:8000/session/get');
  return response;
});
const sessionName = ref(session.value['name']);

</script>

<template>
  <v-app-bar>
    <v-app-bar-title>{{ sessionName }}</v-app-bar-title>
  </v-app-bar>
</template>