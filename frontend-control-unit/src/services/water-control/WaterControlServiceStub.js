import {LetWaterFlow} from "@/services/water-control/WaterControlServiceResponses";

export class WaterControlServiceStub {
    constructor() {
    }

    letWaterFlow() {
        let result = new LetWaterFlow();

        setTimeout(function () {
            let now = new Date();
            result.apiData = {};
            result.loaded = true;
        }, Math.random() * 1500);

        return result;
    }
}
