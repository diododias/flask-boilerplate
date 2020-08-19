from datetime import datetime
from src.interface_adapters.controllers.controller_base import ControllerResourceBase
from src.application_business.services.responses_service import Responses
from src.frameworks_and_drivers.security import Security


class IndexController(ControllerResourceBase):
    @Security.login_required
    def get(self):
        return Responses.ok(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
