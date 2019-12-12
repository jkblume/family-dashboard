import { image1 } from "../StubFixtures.js";


export default class SocketStub {
    constructor(props = {}) {
        this.events = {};
        this.emitted = [];
        Object.assign(this, props);
    }

    on(event, handler) {
        this.events[event] = handler;
    }

    emit(...args) {
        this.emitted = [
            ...this.emitted,
            args
        ];
    }

    simulate(event, payload) {
        this.events[event](payload);
    }

    clear() {
        this.emitted = [];
    }
}

export class SocketIoServiceStub {
    constructor() {
    }

    getActivityNotificationSocket() {
        let socketStub = new SocketStub();
        let now = new Date();
        let events = [{
            activityType: 'STRAVA_ACTIVITY',
            person: {
                name: "Max",
            },
            timestamp: new Date().setHours(now.getHours() - 1),
        }, {
            activityType: 'DETECTED_PERSON',
            person: {
                name: "Max",
            },
            timestamp: new Date().setHours(now.getHours() - 2),
            data: {
                image: image1
            }
        }];
        setInterval(function () {
            let randomEvent = events[Math.floor(Math.random() * events.length)];
            socketStub.simulate('notifications_server', JSON.stringify(randomEvent));
        }, 3000);

        return socketStub;
    }
}