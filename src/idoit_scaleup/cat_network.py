from .consts import C__CATS__NET
from .category import IDoitCategory
from pprint import pprint


class IDoitNetwork(IDoitCategory):

    def __init__(self, cfg):
        super().__init__(cfg, C__CATS__NET)

    def convert_field_with_name_layer2_assignments(self, data):
        rtn = []
        for ele in data['layer2_assignments']:
            rtn.append(int(ele['id']))
        return rtn
