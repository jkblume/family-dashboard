import Vue from "vue";
import App from "@/App.vue";
import router from "@/router";
import DjangoServerService from "@/services/django-server/DjangoServerService";
import SocketIoService from "@/services/socketio-eventbus/SocketIoService";
import WaterControlService from "@/services/water-control/WaterControlService";

Vue.config.productionTip = false;

export const services = new Vue({
  data() {
    const djangoServerService = new DjangoServerService(false, 'http://localhost:8000');
    const socketIoService = new SocketIoService(false, 'http://localhost:8080');
    const waterControlService = new WaterControlService(false, 'http://192.168.178.139');

    return {
      djangoServerService,
      socketIoService,
      waterControlService,
    };
  },
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
