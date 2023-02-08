from .consts import C__CATS__LAYER2_NET
from .category import IDoitCategory
from pprint import pprint


class IDoitVlan(IDoitCategory):

    CATEGORY =  C__CATS__LAYER2_NET

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_standard(self, data):
        return int(data['standard']['value'])

    def convert_field_with_name_layer3_assignments(self, data):
        rtn = []
        for ele in data['layer3_assignments']:
            rtn.append(int(ele['id']))
        return rtn
