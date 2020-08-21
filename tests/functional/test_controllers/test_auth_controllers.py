import pytest
import string
import random

from mock import patch


@patch('src.interface_adapters.controllers.controller_base.ControllerResourceBase.get_json')
@patch('src.application_business.use_cases.filter_user_by_email_usecase.FilterUserByEmailUseCase')
def test_register(find_usecase, mock_get_json, client):
    data = {
        "email": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "password": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
    }

    mock_get_json.return_value = data
    find_usecase.return_value = False

    response = client.post(
        "/auth/register", data=data
    )
    assert response is not None
    assert response.status_code == 201

    find_usecase.return_value = True

    response = client.post(
        "/auth/register", data=data
    )
    assert response is not None
    assert response.status_code == 202
