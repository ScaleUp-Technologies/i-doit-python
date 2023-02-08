from .consts import C__CATG__ACCESS
from .category import IDoitCategory


class IDoitAccess(IDoitCategory):

    CATEGORY = C__CATG__ACCESS

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_primary(self, data):
        return int(data['primary']['value'])
