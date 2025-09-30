<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import AddButton from '@/components/AddButton.vue';
import CreateSessionOverlay from '@/components/overlays/CreateSessionOverlay.vue';
import axios from "axios";

const router = useRouter()
const sessionList = ref([])
const isCreateSessionOverlayVisible = ref(false);

onMounted(async () => {
  try {
    sessionList.value = await axios.get('http://localhost:8000/session/get/saves');
  }
  catch (error) {
    console.log('failed to get session list', error);
  }
});
</script>

<template>
  <v-app-bar app>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-toolbar-title>LLM Game project</v-toolbar-title>
    <v-spacer></v-spacer>
  </v-app-bar>
  <v-container class="flex-grow-1 pa-4 d-flex flex-column">
    <v-list-item v-for="session in sessionList"></v-list-item>
  </v-container>
  <v-main>
    <add-button class="add-button" @click="isCreateSessionOverlayVisible = true"></add-button>
  </v-main>
  <v-overlay v-model="isCreateSessionOverlayVisible" class="overlay-style">
    <create-session-overlay @close-overlay="isCreateSessionOverlayVisible = false"></create-session-overlay>
  </v-overlay>
</template>

<style>
* {
  padding: 0;
  margin: 0;
}
.overlay-style {
  display: flex;
  justify-content: center;
  align-items: center;
}
.add-button {
  position: fixed;
  top: 92%;
  left: 96%;
  width: 50px;
  height: 50px;
}
</style>
