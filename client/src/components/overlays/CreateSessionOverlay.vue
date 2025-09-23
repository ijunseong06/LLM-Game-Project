<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '@/router/index';

const sessionName = ref('');
const sessionDesc = ref('');

const createSession = async () => {
    const response = await axios.post('http://localhost:8000/session/create', null, {
        params: {
            name: sessionName.value,
            desc: sessionDesc.value
        }
    });
    console.log('세션 생성 성공:', response.data)
}

function accessSession(path) {
    router.push({
        name: 'GameSession',
        params: { session : path }
    })
}

 async function confirmProcess() {
    try {
        await createSession();
        accessSession(sessionName.value);
    }
    catch (error) {
        console.error('세션 생성 실패.', error)
    }
    
}
</script>

<template>
    <v-card width="500" max-width="80%" height="220" max-height="50%">
        <v-card-title class="title">{{ $t('createSession') }}</v-card-title>
        <div class="input-container">
            <v-text-field class="text-field-style" :placeholder="$t('createSessionNamePlaceholder')" type="text" v-model="sessionName"></v-text-field>
            <v-text-field class="text-field-style" :placeholder="$t('createSessionDescPlaceholder')" type="text" v-model="sessionDesc"></v-text-field>
        </div>
        <v-card-actions class="justify-end">
            <v-btn color="primary" @click="confirmProcess">{{ $t('createSessionConfirmButton') }}</v-btn>
        </v-card-actions>
    </v-card>
</template>

<style>
.title {
    color: white;
    padding: 15px;
}
.input-container {
    flex-direction: column;
    display: flex;
    gap: 25px;
    margin-left: 15px;
}
.text-field-style {
    color: white;
    background-color: rgb(24, 24, 24);
    width: 40%;
    height: 5vh;
}
</style>