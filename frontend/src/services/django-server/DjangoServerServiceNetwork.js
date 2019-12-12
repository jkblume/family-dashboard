import { responseHandler } from "../Utilities.js";
import {GetEvents} from "@/services/django-server/DjangoServerServiceResponses";

export class DjangoServerServiceNetwork {

  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  getEvents() {
    let result = new GetEvents();
    fetch(this.apiUrl + "/api/events")
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
