from src.interface_adapters.controllers.controller_base import ControllerResourceBase
from src.application_business.services.responses_service import Responses


class IndexController(ControllerResourceBase):

    def get(self):
        return Responses.ok("ok")
