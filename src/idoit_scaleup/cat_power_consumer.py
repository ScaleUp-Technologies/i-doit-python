from .consts import C__CATG__POWER_CONSUMER
from .category import IDoitCategory


class IDoitPowerConsumer(IDoitCategory):

    CATEGORY = C__CATG__POWER_CONUMER

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_active(self, data):
        return int(data['active']['value'])
