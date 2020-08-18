import pytest
from mock import patch
from src.resources.security import Security


@patch('src.resources.security.Security._token_service')
def test_security_login_required(mock_tk_svc):
    mock_tk_svc.decode_auth_token.return_value = {'user_id': True}

    @Security.login_required
    def test_num():
        num = 1
        return num + 1

    assert test_num() == 2

    mock_tk_svc.decode_auth_token.return_value = {'user_id': False}
    with pytest.raises(Exception):
        test_num()
