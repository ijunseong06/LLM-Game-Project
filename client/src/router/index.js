import { createRouter, createWebHistory } from 'vue-router';
import MainView from '@/views/MainView/MainView.vue';
import GameSessionView from '@/views/GameSessionView/GameSessionView.vue';

const routes = [
    {
        path: '/',
        name: 'main',
        component: MainView
    },
    {
        path: '/:session',
        name: 'GameSession',
        component: GameSessionView
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router