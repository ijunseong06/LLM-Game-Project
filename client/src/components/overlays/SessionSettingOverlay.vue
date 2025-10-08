<script setup>
import { ref } from "vue";

const currentSetting = ref('player');

const playerName = ref('');
</script>

<template>
  <v-card
    height="720"
    max-height="80vh"
    width="1280"
    max-width="80vw"
    class="d-flex flex-column"
  >
    <v-card-title class="flex-shrink-0">{{ $t('sessionSettingTitle') }}</v-card-title>
    <v-divider></v-divider>

    <div class="d-flex flex-grow-1">
      
      <v-sheet :width="256" class="border-e">
        <v-list nav dense>
          <v-list-item title="플레이어" @click="currentSetting = 'player'" :active="currentSetting === 'player'"></v-list-item>
        </v-list>
      </v-sheet>

      <div class="pa-4 flex-grow-1">
        <div v-if="currentSetting === 'player'">
          <h3 class="mb-4">플레이어 설정</h3>
          <v-text-field label="이름" variant="outlined" style="max-width: 400px;" v-model="playerName"></v-text-field>
        </div>
        
        <div v-else>
          <p>왼쪽에서 설정할 항목을 선택하세요.</p>
        </div>
      </div>
    </div>
  </v-card>
</template>