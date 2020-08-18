from src.application_business.services.responses_service import Responses


def error_handler(e):
    return Responses.bad_request(e)
