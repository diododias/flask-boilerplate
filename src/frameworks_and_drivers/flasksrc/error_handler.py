from src.application_business.services.responses_service import Responses
from flask import abort


def error_handler(e):
    return abort(Responses.bad_request(e))
