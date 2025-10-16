<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const currentSetting = ref('player');

const playerName = ref('');
const playerGender = ref('');
const playerAge = ref(0);
const playerRace = ref('');
const playerAppearence = ref('');

const saveSettings = async () => {
  localStorage.setItem('playerName', playerName.value);
  localStorage.setItem('playerGender', playerGender.value);
  localStorage.setItem('playerAge', playerAge.value);
  localStorage.setItem('playerRace', playerRace.value);
  localStorage.setItem('playerAppearence', playerAppearence.value);
  await axios.post('http://localhost:8000/session/save/player', null, {
    params: {
      name: localStorage.getItem('playerName'),
      gender: localStorage.getItem('playerGender'),
      age: localStorage.getItem('playerAge'),
      race: localStorage.getItem('playerRace'),
      appearence: localStorage.getItem('playerAppearence')
    }
  });
};

onMounted(async () => {
  playerName.value = localStorage.getItem('playerName') || '';
  playerGender.value = localStorage.getItem('playerGender') || '';
  playerAge.value = localStorage.getItem('playerAge') || '';
  playerRace.value = localStorage.getItem('playerRace') || '';
  playerAppearence.value = localStorage.getItem('playerAppearence') || '';
});
</script>

<template>
  <v-card height="720" max-height="80vh" width="1280" max-width="80vw" class="d-flex flex-column">
    <div class="d-flex justify-space-between align-center flex-shrink-0">
      <v-card-title>{{ $t('sessionSettingTitle') }}</v-card-title>
      
      <div class="pa-4">
        <v-btn color="primary" @click="saveSettings">
          {{ $t('sessionSettingSave') }}
        </v-btn>
      </div>
    </div>
    <v-divider></v-divider>

    <div class="d-flex flex-grow-1">
      
      <v-sheet :width="256" class="border-e">
        <v-list nav dense>
          <v-list-item :title="$t('sessionSettingPlayerHeader')" @click="currentSetting = 'player'" :active="currentSetting === 'player'"></v-list-item>
        </v-list>
      </v-sheet>

      <div class="pa-4 flex-grow-1">
        <div v-if="currentSetting === 'player'">
          <h3 class="mb-4">{{ $t('sessionSettingPlayerSubheader') }}</h3>
          <v-textarea :label="$t('sessionSettingPlayerName')" variant="outlined" style="max-width: 400px;" v-model="playerName" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerGender')" variant="outlined" style="max-width: 400px;" v-model="playerGender" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerAge')" variant="outlined" style="max-width: 400px;" v-model="playerAge" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerRace')" variant="outlined" style="max-width: 400px;" v-model="playerRace" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerAppearence')" variant="outlined" style="max-width: 400px;" v-model="playerAppearence" auto-grow rows="1"></v-textarea>
        </div>
        
        <div v-else>
          <p></p>
        </div>
      </div>
    </div>
  </v-card>
</template>