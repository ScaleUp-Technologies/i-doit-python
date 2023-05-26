from .consts import C__CATG__NETWORK_LOG_PORT, C__CATG__IP, C__CATG__NETWORK_PORT
from .category import IDoitCategory
from copy import deepcopy


class IDoitNetworkLogicalPort(IDoitCategory):

    CATEGORY = C__CATG__NETWORK_LOG_PORT

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)

    def convert_field_with_name_active(self, data):
        return int(data['active']['value'])

    def convert_field_with_name_interface(self, data):
        if len(data['interface']) == 0:
            return None
        return int(data['interface'][0]['id'])

    def convert_field_with_name_addresses(self, data):
        return self.convert_list(data['addresses'])

    def convert_field_with_name_layer2_assignment(self, data):
        if data['layer2_assignment'] == []:
            return None
        # else:
        raise Exception('unknown conversion ', data)

    def convert_field_with_name_assigned_connector(self, data):
        return self.conv_array_field('assigned_connector', data, 'ref_id')

    def convert_field_with_name_net(self, data):
        return self.convert_list(data['net'])

    def save_category_if_changed(self, objId, data):
        raise Exception(
            'Funktioniert nur wenn es nur eine Kategorie gibt, ' +
            'muss mit ID spezifiziert werden')

    def fix_obj(self, cdata):
        if ('interface' in cdata.keys()) and (cdata['interface'] is not None):
            cdata['interface'] = "%d_C__CATG__NETWORK_INTERFACE" % cdata['interface']
        if ('addresses' in cdata.keys()) and (cdata['addresses'] is not None):
            rtn = []
            for ele in cdata['addresses']:
                rtn.append(str(ele))
            cdata['addresses'] = rtn

        if ('ports' in cdata.keys()) and (cdata['ports'] is not None):
            rtn = []
            for ele in cdata['ports']:
                rtn.append("%d_%s" % (ele, C__CATG__NETWORK_PORT))
            cdata['ports'] = rtn

    def save_category(self, objId, data):
        cdata = deepcopy(data)
        self.fix_obj(cdata)
        return super().save_category(objId, cdata)

    def update_category(self, objId, data):
        cdata = deepcopy(data)
        self.fix_obj(cdata)
        return super().update_category(objId, cdata)
