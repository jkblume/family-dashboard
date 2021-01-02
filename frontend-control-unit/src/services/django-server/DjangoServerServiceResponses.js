import APIResult from "@/services/APIResult";

export class GetEvents extends APIResult {
  constructor() {
    super();
    this.apiData = [];
  }
}