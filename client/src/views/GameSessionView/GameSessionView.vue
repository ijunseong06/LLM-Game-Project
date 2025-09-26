<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const session = ref({})
const sessionName = ref('');

const confirmInput = async () => {
  const response = await axios.get('http://localhost:8000')
}

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
  <v-main class="d-flex flex-column">
    <v-container class="flex-grow-1 pa-4 d-flex flex-column">
      <v-textarea variant="plain" class="scrollable-textarea flex-grow-1" hide-details style="overflow-y: auto;" readonly></v-textarea>
    </v-container>
    <v-container class="flex-shrink-0">
      <v-textarea :placeholder="$t('inGameInputField')" variant="outlined" auto-grow rows="1" @keydown.ctrl.enter.prevent="console.log('test')">
      </v-textarea>
    </v-container>
  </v-main>
</template>