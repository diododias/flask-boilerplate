from datetime import datetime
from src.frameworks_and_drivers.cache import cache
from src.interface_adapters.controllers.controller_base import ControllerResourceBase
from src.application_business.services.responses_service import Responses


class IndexController(ControllerResourceBase):
    def get(self):
        @cache.memoize(300)
        def return_message():
            return datetime.now()

        return Responses.ok(return_message().strftime("%Y-%m-%d %H:%M:%S"))
