import { image1, image2 } from "../StubFixtures.js";


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
        let events = [
            {
                activityType: 'STRAVA_ACTIVITY',
                data: {
                    person: {
                        name: "Max",
                    },
                }, 
                timestamp: new Date().setHours(now.getHours() - 1),
            }, 
            {
                activityType: 'DETECTED_PERSON',
                timestamp: new Date().setHours(now.getHours() - 2),
                data: {
                    image: image1,
                    person: {
                        name: "Max",
                    }
                }
            }, 
            {
                activityType: 'DETECTED_PERSON',
                timestamp: new Date().setHours(now.getHours() - 3),
                data: {
                    image: image2,
                    person: {
                        name: "Scarlett Johansson",
                    }
                }
            }, 
            {
                activityType: 'RANDOM_GOOGLE_PHOTO',
                timestamp: new Date().setHours(now.getHours() - 3),
                data: {
                    privateUrl: "1234",
                    publicUrl: "https://cdn1.stuttgarter-zeitung.de/media.media.3da7e7c2-d328-47e0-b0fd-458154fdd1b1.original1024.jpg",
                    creationTime: "2019-11-23T15:04:46Z",
                    person: {
                        name: "Max",
                    },
                }
            }
        ];
        setInterval(function () {
            let randomEvent = events[Math.floor(Math.random() * events.length)];
            socketStub.simulate('notifications_server_eventstream', JSON.stringify(randomEvent));
        }, 3000);

        return socketStub;
    }
}