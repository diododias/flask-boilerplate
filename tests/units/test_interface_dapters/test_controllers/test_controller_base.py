from mock import MagicMock
from src.interface_adapters.controllers.controller_base import ControllerResourceBase


def test_controller_base_get_headers():
    service_mock = MagicMock()
    request_mock = MagicMock()
    controller = ControllerResourceBase(token_service=service_mock, flask_request=request_mock)
    request_mock.headers = dict()

    result = controller.get_headers()

    assert isinstance(result, dict)


def test_controller_base_get_json():
    service_mock = MagicMock()
    request_mock = MagicMock()
    controller = ControllerResourceBase(token_service=service_mock, flask_request=request_mock)

    controller.get_json()

    request_mock.get_json.assert_called()


def test_controller_base_get_token():
    service_mock = MagicMock()
    request_mock = MagicMock()
    controller = ControllerResourceBase(token_service=service_mock, flask_request=request_mock)

    service_mock.decode_auth_token.return_value = {'auth_token': ""}
    controller.get_token()

    service_mock.decode_auth_token.assert_called()


def test_controller_base_get_user_id():
    service_mock = MagicMock()
    request_mock = MagicMock()
    controller = ControllerResourceBase(token_service=service_mock, flask_request=request_mock)

    service_mock.decode_auth_token.return_value = {'user_id': ""}
    controller.get_user_id()

    service_mock.decode_auth_token.assert_called()
