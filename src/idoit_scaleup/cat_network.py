from .consts import C__CATS__NET
from .category import IDoitCategory
from pprint import pprint


class IDoitNetwork(IDoitCategory):

    CATEGORY = C__CATS__NET

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_layer2_assignments(self, data):
        rtn = []
        for ele in data['layer2_assignments']:
            rtn.append(int(ele['id']))
        return rtn
