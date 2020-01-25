from typing import Union


class ResponseDataBuilder:
    @staticmethod
    def build_error_response(error_message: str, error_code: str = None) -> dict:
        return {"error": {"message": error_message, "code": error_code}}

    @staticmethod
    def build_success_response(data: Union[list, dict]) -> dict:
        return {"data": data}
