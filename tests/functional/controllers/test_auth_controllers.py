import pytest
from mock import patch


@patch('src.interface_adapters.controllers.controller_base.ControllerResourceBase.get_json')
def test_register(mock_get_json, client):
    data = {"email": 'test@test.com', "password": '1234567'}
    mock_get_json.return_value = data

    response = client.post(
        "/auth/register", data=data
    )
    assert response is not None
    assert response.status_code == 202
