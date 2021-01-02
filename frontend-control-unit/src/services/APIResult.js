export default class APIResult {
  constructor() {
    this.error = null;
    this.loaded = false;
  }

  hasLoaded() {
    return this.loaded && this.error === null;
  }
}
