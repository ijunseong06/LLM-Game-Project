<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const sessionName = ref('');

const drawerShow = ref(false);

const inputMessage = ref('');
const outputMessage = ref('');

const confirmInput = async () => {
  localStorage.setItem('currentInput', inputMessage.value);
  inputMessage.value = '';
  const response = await axios.post('http://localhost:8000/llm/response/generate', null, {
    params: {
      input: localStorage.getItem('currentInput')
    }
  });
  outputMessage.value += response.data['response'];
  saveSession();
}

const saveSession = async () => {
  await axios.post('http://localhost:8000/session/save', null, {
    params: {
      name: localStorage.getItem('sessionName'),
      description: localStorage.getItem('sessionDesc')
    }
  });
}

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/session/get');
    const historyList = response.data['history'];
    outputMessage.value = historyList.map(item => item.content)
    sessionName.value = localStorage.getItem('sessionName');
  }
  catch (error) {
    console.error("Failed to fetch session data:", error);
  }
});
</script>

<template>
  <v-app-bar>
    <v-app-bar-nav-icon @click.stop="drawerShow = !drawerShow"></v-app-bar-nav-icon>
    <v-app-bar-title>{{ sessionName }}</v-app-bar-title>
  </v-app-bar>
  <v-main class="d-flex flex-column">
    <v-container class="flex-grow-1 pa-4 d-flex flex-column">
      <v-textarea variant="plain" class="scrollable-textarea flex-grow-1" hide-details style="overflow-y: auto;" readonly v-model="outputMessage"></v-textarea>
    </v-container>
    <v-container class="flex-shrink-0">
      <v-textarea :placeholder="$t('inGameInputField')" variant="outlined" auto-grow rows="1" @keydown.ctrl.enter.prevent="confirmInput" v-model="inputMessage"></v-textarea>
    </v-container>
  </v-main>
</template>