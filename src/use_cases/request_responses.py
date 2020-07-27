import json
from flask import Response


def response_base(response_value: dict or list or str, status_code: int) -> Response:
    """
        Response base return request status code
        :param response_value:  object returned to API consumer
        :param status_code: status code of response returned
        :return: Response object
        """
    return Response(json.dumps({
        "status": 'success',
        "data": response_value
    }),
        mimetype='application/json',
        status=status_code)


def response_ok(response_value: dict or list or str) -> Response:
    """
    Response ok return status code 200
    :param response_value: json data returned to api consumer
    :return: Response object
    """

    return response_base(response_value, 200)


def response_bad_request(response_value: dict or list or str) -> Response:
    """
    Response bad request return status code 400
    :param response_value: json data returned to api consumer
    :return: Response object
    """
    return response_base(response_value, 400)


def response_not_found(response_value: dict or list or str) -> Response:
    """
    Response type not found return status code 404
    :param response_value: display error message
    :return: Response object
    """
    return response_base(response_value, 404)
