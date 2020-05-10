import Router from 'vue-router'
import Index from './components/pages/Index'
import Vue from 'vue'
import sendDiaryView from './components/pages/SendDiaryView'


Vue.use(Router);


export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'index',
            component: Index,
        },
        {
            path: '/sendDiary',
            name: 'sendDiary',
            component: sendDiaryView
        },
    ]
})
