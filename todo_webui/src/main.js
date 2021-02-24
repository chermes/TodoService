import Vue from 'vue';
import App from './App.vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import Axios from 'axios';

Vue.config.productionTip = false;

Axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;

Vue.use(Buefy);

new Vue({
  render: h => h(App),
}).$mount('#app')
