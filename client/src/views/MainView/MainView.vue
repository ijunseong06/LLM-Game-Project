<script setup>
import { onMounted, ref } from 'vue';
import AddButton from '@/components/AddButton.vue';
import CreateSessionOverlay from '@/components/overlays/CreateSessionOverlay.vue';
import axios from "axios";
import router from '@/router';

const sessionList = ref([])
const isCreateSessionOverlayVisible = ref(false);

const loadSession = (async (index) => {
  localStorage.setItem('sessionName', sessionList.value[index]['name']);
  localStorage.setItem('sessionDesc', sessionList.value[index]['description']);
  await axios.post('http://localhost:8000/session/load', null, {
    params: {
      name: sessionList.value[index]['name']
    }
  })
  router.push({
        name: 'GameSession',
        params: { session : sessionList.value[index]['name'] }
  });
});

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/session/get/saves');
    sessionList.value = response.data;
  }
  catch (error) {
    console.log('failed to get session list', error);
  }
});
</script>

<template>
  <v-app-bar app>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-toolbar-title>LLM Game Project</v-toolbar-title>
    <v-spacer></v-spacer>
  </v-app-bar>
  <v-main>
    <v-container class="flex-grow-1 pa-4 d-flex flex-column">
      <v-row v-if="sessionList != null && sessionList.length > 0">
        <v-col
          v-for="(session, index) in sessionList" :key="index" cols="12" sm="6" lg="4">
          <v-card height="100%" @click="loadSession(index)">
            <v-card-title>{{ session['name'] }}</v-card-title>
            <v-card-text>{{ session['description'] }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
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
