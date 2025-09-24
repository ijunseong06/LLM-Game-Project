<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const session = ref({})
const sessionName = ref('');

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/session/get');
    session.value = response.data;
    sessionName.value = session.value['name'];
  }
  catch (error) {
    console.error("Failed to fetch session data:", error);
  }
});
</script>

<template>
  <v-app-bar>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-app-bar-title>{{ sessionName }}</v-app-bar-title>
  </v-app-bar>
</template>