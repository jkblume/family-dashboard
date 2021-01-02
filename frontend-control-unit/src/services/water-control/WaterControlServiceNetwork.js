import { responseHandler } from "../Utilities.js";
import {LetWaterFlow} from "@/services/water-control/WaterControlServiceResponses";

export class WaterControlServiceNetwork {

  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  letWaterFlow(duration) {
    let result = new LetWaterFlow();
    fetch(this.apiUrl + "/let?command=" + duration)
      .then(responseHandler)
      .then((json) => {
        result.apiData = json.data;
        result.loaded = true;
      })
      .catch((error) => {
        console.error(error);
        result.loaded = true;
        result.error = error;
      });
    return result;
  }

}
