from .consts import C__CATG__APPLICATION
from .category import IDoitCategory
from copy import deepcopy

class IDoitApplication(IDoitCategory):

    CATEGORY = C__CATG__APPLICATION

    def __init__(self, cfg):
        super().__init__(cfg, self.CATEGORY)


    # FIXME Skip, must be implemented later
    def convert_field_with_name_assigned_license(self, data):
        return 0

    # FIXME Skip, must be implemented later
    def convert_field_with_name_assigned_database_schema(self, data):
        return 0

    # FIXME Skip, must be implemented later
    def convert_field_with_name_assigned_it_service(self, data):
        return 0

    def convert_field_with_name_assigned_version(self, data):
        return int(data['assigned_version']['ref_id'])

    def convert_field_with_name_bequest_nagios_services(self, data):
        return int(data['bequest_nagios_services']['value'])
#    def fix_obj(self, cdata):
#        if ('assigned_version' in cdata.keys()) and (cdata['assigned_version'] is not None):
#            cdata['assigned_version'] = str(cdata['assigned_version'])

#    def save_category(self, objId, data):
#        cdata = deepcopy(data)
#        self.fix_obj(cdata)
#        return super().save_category(objId, cdata)

#    def update_category(self, objId, data):
#        cdata = deepcopy(data)
#        self.fix_obj(cdata)
#        return super().update_category(objId, cdata)
