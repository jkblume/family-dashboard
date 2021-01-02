import {WaterControlServiceNetwork} from "@/services/water-control/WaterControlServiceNetwork";
import {WaterControlServiceStub} from "@/services/water-control/WaterControlServiceStub";

export default class WaterControlService {
  constructor(useStub, apiUrl) {
    this.useStub = useStub;
    this.apiUrl = apiUrl;
  }

  letWaterFlow(duration) {
    if (this.useStub) {
      console.info("Using Stub data for WaterControlService!");
      return new WaterControlServiceStub().letWaterFlow(duration);
    }
    return new WaterControlServiceNetwork(this.apiUrl).letWaterFlow(duration);
  }

}
