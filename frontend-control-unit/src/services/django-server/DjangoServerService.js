import {DjangoServerServiceNetwork} from "@/services/django-server/DjangoServerServiceNetwork";
import {DjangoServiceStub} from "@/services/django-server/DjangoServiceStub";

export default class DjangoServerService {
  constructor(useStub, apiUrl) {
    this.useStub = useStub;
    this.apiUrl = apiUrl;
  }

  getEvents() {
    if (this.useStub) {
      console.info("Using Stub data for DjangoServerService!");
      return new DjangoServiceStub().getEvents();
    }
    return new DjangoServerServiceNetwork(this.apiUrl).getEvents();
  }

}
