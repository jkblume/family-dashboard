import { image1 } from "../StubFixtures.js";
import {GetEvents} from "@/services/django-server/DjangoServerServiceResponses";

export class DjangoServiceStub {
    constructor() {
    }

    getEvents() {
        let result = new GetEvents();

        setTimeout(function () {
            let now = new Date();
            result.apiData = [
                {
                    activityType: 'STRAVA_ACTIVITY',
                    person: {
                        name: "Max",
                    },
                    timestamp: new Date().setHours(now.getHours() - 1),
                },
                {
                    activityType: 'DETECTED_PERSON',
                    person: {
                        name: "Max",
                    },
                    timestamp: new Date().setHours(now.getHours() - 2),
                    data: {
                        image: image1
                    }
                },
                {
                    activityType: 'DETECTED_PERSON',
                    // person: {
                    //     name: "Max",
                    // },
                    timestamp: new Date().setHours(now.getHours() - 3),
                    data: {
                        image: image1
                    }
                }
            ];
            result.loaded = true;
        }, Math.random() * 1500);

        return result;
    }
}
