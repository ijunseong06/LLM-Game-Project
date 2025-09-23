<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AddButton from '@/components/AddButton.vue';
import CreateSessionOverlay from '@/components/overlays/CreateSessionOverlay.vue';

const router = useRouter()
const isCreateSessionOverlayVisible = ref(false);
</script>

<template>
  <v-app-bar app>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-toolbar-title>LLM Game project</v-toolbar-title>
    <v-spacer></v-spacer>
  </v-app-bar>
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
