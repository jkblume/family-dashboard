import io from 'socket.io-client';

export class SocketIoServiceNetwork {

  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  getActivityNotificationSocket() {
    return io(this.apiUrl);
  }

}
