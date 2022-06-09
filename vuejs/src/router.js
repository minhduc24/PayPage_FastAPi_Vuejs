import { createRouter, createWebHistory } from 'vue-router'
import Home from './view/Home.vue'
import Account from './view/Account.vue'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Home },
        { path: '/account', component: Account }
    ]
})

export default router