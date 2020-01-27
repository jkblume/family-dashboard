import Vue from "vue";
import App from "@/App.vue";
import router from "@/router";
import DjangoServerService from "@/services/django-server/DjangoServerService";
import SocketIoService from "@/services/socketio-eventbus/SocketIoService";

Vue.config.productionTip = false;

export const services = new Vue({
  data() {
    const djangoServerService = new DjangoServerService(true, 'http://localhost:8000');
    const socketIoService = new SocketIoService(true, 'http://localhost:8080');

    return {
      djangoServerService,
      socketIoService,
    };
  },
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
