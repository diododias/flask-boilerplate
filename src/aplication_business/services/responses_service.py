import json
from flask import Response


class Responses:
    @staticmethod
    def response_base(data: dict or list or str = list(),
                      status_code: int = 200,
                      message: str or list = list(),
                      status_message: str = "success") -> Response:
        """
            Response base return request status code
            :param data: Response data
            :param status_code: status code of response returned
            :param status_message: status message informing success or fail
            :param message: message information to the user
            :return: Response object
            """
        return Response(json.dumps({
            "status": status_message,
            "data": data,
            "message": message
        }),
            mimetype='application/json',
            status=status_code)

    @staticmethod
    def ok(data: dict or list or str = list(), message: list or str = list()) -> Response:
        """
        Response ok return status code 200
        :param data: json data returned to api consumer
        :param message: message information to the user
        :return: Response object
        """

        return Responses.response_base(data=data, message=message, status_code=200)

    @staticmethod
    def created(response_value: dict or list or str = list()) -> Response:
        """
        Response ok return status code 200
        :param response_value: json data returned to api consumer
        :return: Response object
        """

        return Responses.response_base(data=response_value, status_code=201)

    @staticmethod
    def accepted(response_value: dict or list or str = list(), message: str or dict or list = list()) -> Response:
        """
        Response ok return status code 200
        :param response_value: json data returned to api consumer
        :param message: message to inform API user
        :return: Response object
        """
        return Responses.response_base(data=response_value, message=message, status_code=202)

    @staticmethod
    def bad_request(message: str or dict or list = list()) -> Response:
        """
        Response bad request return status code 400
        :param message: json data returned to api consumer
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=400, status_message="fail")

    @staticmethod
    def not_found(message: dict or list or str = 'Not found') -> Response:
        """
        Response type not found return status code 404
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=404, status_message="fail")

    @staticmethod
    def unauthorized(message: dict or list or str = "Unauthorized access") -> Response:
        """
        Response type not found return status code 404
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=401, status_message="fail")

    @staticmethod
    def invalid_entity(message: dict or list or str = "Invalid field") -> Response:
        """
        Response type not found return status code 404
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=422, status_message="fail")
