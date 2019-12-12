export async function responseHandler(response) {
  let statusMessage = "Error occurred with status " + response.status;
  if (response.status !== 200) {
    let errorMessage;
    try {
      let json = await response.json();
      let error = json.error;
      errorMessage = statusMessage + ": " + error.message;
    } catch (err) {
      errorMessage = statusMessage;
    }
    throw new ApiError(response.status, errorMessage);
  }
  return response.json();
}

export class ApiError extends Error {
  constructor(status, ...args) {
    super(...args);
    this.status = status;
  }
}
