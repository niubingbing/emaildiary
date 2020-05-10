import Vue from 'vue'
import router from './router'
import App from './App'
import 'wired-elements'
import apolloProvider from './apollo'


Vue.config.productionTip = false;

new Vue({
    router,
    apolloProvider,
    render: h => h(App)
}).$mount('#app');


