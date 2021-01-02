import {SocketIoServiceNetwork} from "@/services/socketio-eventbus/SocketIoServiceNetwork";
import {SocketIoServiceStub} from "@/services/socketio-eventbus/SocketIoServiceStub";

export default class SocketIoService {
  constructor(useStub, apiUrl) {
    this.useStub = useStub;
    this.apiUrl = apiUrl;
  }

  getActivityNotificationSocket() {
    if (this.useStub) {
      console.info("Using Stub data for SocketIoServiceStub!");
      return new SocketIoServiceStub().getActivityNotificationSocket();
    }
    return new SocketIoServiceNetwork(this.apiUrl).getActivityNotificationSocket();
  }

}
