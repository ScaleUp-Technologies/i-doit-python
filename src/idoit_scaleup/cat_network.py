from .consts import C__CATS__NET
from .category import IDoitCategory
from pprint import pprint
from copy import deepcopy
from ipaddress import IPv4Network
from ipaddress import IPv6Network


class IDoitNetwork(IDoitCategory):

    CATEGORY = C__CATS__NET

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_layer2_assignments(self, data):
        rtn = []
        for ele in data['layer2_assignments']:
            rtn.append(int(ele['id']))
        return rtn

    def fix_mask_and_range(self, data):
        net_str=f"{data['address']}/{data['cidr_suffix']}"
        if int(data['type'])==1:
            net= IPv4Network(net_str)
        elif int(data['type'])==1000:
            net= IPv6Network(net_str)
        data['netmask']= str(net.netmask)
        data['range_from'] = str(net[0])
        data['range_to'] = str(net[-1])

    def save_category(self, objId, data):
        cdata = deepcopy(data)
        self.fix_mask_and_range(cdata)
        return super().save_category(objId, cdata)

    def update_category(self, objId, data):
        cdata = deepcopy(data)
        self.fix_mask_and_range(cdata)
        return super().update_category(objId, cdata)
