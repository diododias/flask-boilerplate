import json
from flask import Response


class Responses:
    @staticmethod
    def response_base(data=None,
                      status_code: int = 200,
                      message=None,
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
    def ok(data="", message="") -> Response:
        """
        Response ok return status code 200
        :param data: json data returned to api consumer
        :param message: message information to the user
        :return: Response object
        """

        return Responses.response_base(data=data, message=message, status_code=200)

    @staticmethod
    def created(response_value) -> Response:
        """
        Response created return status code 201
        :param response_value:
        :return:
        """
        return Responses.response_base(data=response_value, status_code=201)

    @staticmethod
    def accepted(data="", message="") -> Response:
        """
        Response accepted return status code 202
        :param data: any data of response
        :param message: message to inform user
        :return:
        """
        return Responses.response_base(data=data, message=message, status_code=202)

    @staticmethod
    def bad_request(message="Bad request") -> Response:
        """
        Response bad request return status code 400
        :param message: json data returned to api consumer
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=400, status_message="fail")

    @staticmethod
    def not_found(message='Not found') -> Response:
        """
        Response type not found return status code 404
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=404, status_message="fail")

    @staticmethod
    def unauthorized(message="Unauthorized access") -> Response:
        """
        Response type access unauthorized
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=401, status_message="fail")

    @staticmethod
    def invalid_entity(message="Invalid field") -> Response:
        """
        Response type Invalid Entity
        :param message: display error message
        :return: Response object
        """
        return Responses.response_base(message=message, status_code=422, status_message="fail")
