<script setup lang="ts">
import { onMounted, ref, Ref } from "vue";
import axios from "axios";

const currentSetting = ref('player');

const playerName : Ref<string> = ref('');
const playerGender : Ref<string> = ref('');
const playerAge : Ref<string> = ref('');
const playerRace : Ref<string> = ref('');
const playerAppearence : Ref<string> = ref('');
const playerPersonality : Ref<string> = ref('');
const playerBackground : Ref<string> = ref('');
const playerNote : Ref<string> = ref('');

const statsListText : Ref<string> = ref('');
const statsList : Ref<string[]> = ref(['']);

const saveSettings = async () => {
  localStorage.setItem('playerName', playerName.value);
  localStorage.setItem('playerGender', playerGender.value);
  localStorage.setItem('playerAge', playerAge.value);
  localStorage.setItem('playerRace', playerRace.value);
  localStorage.setItem('playerAppearence', playerAppearence.value);
  localStorage.setItem('playerPersonality', playerPersonality.value);
  localStorage.setItem('playerBackground', playerBackground.value);
  localStorage.setItem('playerNote', playerNote.value);

  statsList.value = await statsToList();
  localStorage.setItem('statsList', JSON.stringify(statsList.value));

  await axios.post('http://localhost:8000/session/setting/player', null, {
    params: {
      name: localStorage.getItem('playerName'),
      gender: localStorage.getItem('playerGender'),
      age: localStorage.getItem('playerAge'),
      race: localStorage.getItem('playerRace'),
      appearence: localStorage.getItem('playerAppearence'),
      personality: localStorage.getItem('playerPersonality'),
      background: localStorage.getItem('playerBackground'),
      note: localStorage.getItem('playerNote')
    }
  });
  await axios.post('http://localhost:8000/session/setting/general', null, {
    params: {
      stats: localStorage.getItem('statsList')
    }
  });
};

const statsToList = async () : Promise<string[]> => {
  return statsListText.value.split(',').map(item => item.trim()).filter(item => item.length > 0);
}

onMounted(async () => {
  playerName.value = localStorage.getItem('playerName') || '';
  playerGender.value = localStorage.getItem('playerGender') || '';
  playerAge.value = localStorage.getItem('playerAge') || '';
  playerRace.value = localStorage.getItem('playerRace') || '';
  playerAppearence.value = localStorage.getItem('playerAppearence') || '';
  playerPersonality.value = localStorage.getItem('playerPersonality') || '';
  playerBackground.value = localStorage.getItem('playerBackground') || '';
  playerNote.value = localStorage.getItem('playerNote') || '';

  statsList.value = JSON.parse(localStorage.getItem('statsList')) || [''];
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
          <v-list-item :title="$t('sessionSettingGeneralHeader')" @click="currentSetting = 'general'" :active="currentSetting === 'general'"></v-list-item>
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
          <v-textarea :label="$t('sessionSettingPlayerPersonality')" variant="outlined" style="max-width: 400px;" v-model="playerPersonality" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerBackground')" variant="outlined" style="max-width: 400px;" v-model="playerBackground" auto-grow rows="1"></v-textarea>
          <v-textarea :label="$t('sessionSettingPlayerNote')" variant="outlined" style="max-width: 400px;" v-model="playerNote" auto-grow rows="1"></v-textarea>
        </div>
        <div v-if="currentSetting === 'general'">
          <h3 class="mb-4">{{ $t('sessionSettingGeneralHeader') }}</h3>
          <v-textarea :label="$t('sessionSettingGeneralStatsList')" variant="outlined" v-model="statsListText" style="max-width: 400px;" auto-grow rows="1"></v-textarea>
        </div>
        
        <div v-else>
          <p></p>
        </div>
      </div>
    </div>
  </v-card>
</template>