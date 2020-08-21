import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')

import pytest
import uuid
from flask import request
from mock import patch, MagicMock
from src.application_business.services.token_service import TokenService
from src.application_business.interfaces.create_token_entity_usecase import ICreateTokenEntityUseCase
from src.application_business.interfaces.filter_token_by_token_usecase import IFilterTokenByTokenUseCase
from src.application_business.interfaces.get_auth_token_usecase import IGetAuthTokenUseCase
from src.application_business.interfaces.invalidate_token_usecase import IInvalidateTokenUseCase

rq = MagicMock(spec=request)


def create_token_service(create_token_entity_usecase=MagicMock(spec=ICreateTokenEntityUseCase),
                         filter_token_by_token_usecase=MagicMock(spec=IFilterTokenByTokenUseCase),
                         invalidate_token_usecase=MagicMock(spec=IInvalidateTokenUseCase),
                         get_auth_token=MagicMock(spec=IGetAuthTokenUseCase),
                         secret=""):
    return TokenService(create_token_entity_usecase=create_token_entity_usecase,
                        filter_token_by_token_usecase=filter_token_by_token_usecase,
                        invalidate_token_usecase=invalidate_token_usecase,
                        get_auth_token=get_auth_token,
                        secret=secret)


def test_invalid_token_service_is_blacklisted():
    filter_token_mock = MagicMock(spec=IFilterTokenByTokenUseCase)
    token_service = create_token_service(filter_token_by_token_usecase=filter_token_mock)

    filter_token_mock.execute.return_value = True
    assert token_service.is_blacklisted("TOKEN") is True

    filter_token_mock.execute.return_value = None
    assert token_service.is_blacklisted("TOKEN") is False


def test_invalid_token_service_include_token_blacklist():
    invalidate_token_mock = MagicMock(spec=IInvalidateTokenUseCase)
    filter_token_mock = MagicMock(spec=IFilterTokenByTokenUseCase)
    create_entity_mock = MagicMock(spec=ICreateTokenEntityUseCase)
    token_service = create_token_service(create_token_entity_usecase=create_entity_mock,
                                         filter_token_by_token_usecase=filter_token_mock,
                                         invalidate_token_usecase=invalidate_token_mock)

    filter_token_mock.execute.return_value = True
    create_entity_mock.execute.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True

    filter_token_mock.execute.return_value = None
    create_entity_mock.execute.return_value = False
    invalidate_token_mock.execute.return_value = True
    assert token_service.include_token_blacklist("TOKEN") is True
    invalidate_token_mock.execute.assert_called()


def test_decode_auth_token_invalid_token():
    get_token_mock = MagicMock(spec=IGetAuthTokenUseCase)
    filter_token_mock = MagicMock(spec=IFilterTokenByTokenUseCase)
    token_service = create_token_service(filter_token_by_token_usecase=filter_token_mock,
                                         get_auth_token=get_token_mock)

    get_token_mock.execute.return_value = False
    with pytest.raises(Exception):
        token_service.decode_auth_token()

    get_token_mock.execute.return_value = "INVALID TOKEN"
    with pytest.raises(Exception):
        token_service.decode_auth_token()



def test_decode_auth_token_successfull():
    get_token_mock = MagicMock(spec=IGetAuthTokenUseCase)
    filter_token_mock = MagicMock(spec=IFilterTokenByTokenUseCase)
    token_service = create_token_service(get_auth_token=get_token_mock,
                                         filter_token_by_token_usecase=filter_token_mock)

    uuid_mocked = token_service.encode_auth_token(str(uuid.uuid4()))
    get_token_mock.execute.return_value = uuid_mocked

    filter_token_mock.execute.return_value = False

    decoded = token_service.decode_auth_token()

    assert decoded is not None
    assert decoded.get('user_id', None) is not None
    assert decoded.get('auth_token', None) is not None
    assert decoded.get('auth_token') == uuid_mocked
