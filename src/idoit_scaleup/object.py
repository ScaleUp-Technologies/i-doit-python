from typing import List
from .base import IDoitApiBase


class IDoitObject(IDoitApiBase):
    def __init__(self, cfg, obj_type: str):
        super().__init__(cfg)
        self.obj_type = obj_type

    def get_by_title(self, title: str, categories: List = []):
        params = {
            'filter': {
                'type': self.obj_type,
                'title': title,
            },
        }
        if len(categories) > 0:
            params['categories'] = categories
        rtn = self.xml_rpc_call('cmdb.objects', params)
        if len(rtn['result']) == 0:
            return None
        else:
            return rtn['result'][0]

    def get_all(self, categories: List = []):
        params = {
            'filter': {
                'type': self.obj_type
            },
        }
        if len(categories) > 0:
            params['categories'] = categories
        rtn = self.xml_rpc_call('cmdb.objects', params)
        return rtn['result']

    def create_object_with_title(self, title: str):
        params = {
            'title': title,
            'type': self.obj_type
        }
        return self.xml_rpc_call('cmdb.object.create', params)

    def create_object_if_not_there(self, title):
        obj = self.get_by_title(title)
        if obj is None:
            r = self.create_object_with_title(title)
            print('-------------------')
            print("%s  (%s) " % (title, self.obj_type))
            print('-------------------')
            objId = r['result']['id']
        else:
            objId = obj['id']
        return objId

    def update_object(self, obj_id: str, title: str):
        params = {
            'id': obj_id,
            'title': title,
        }
        return self.xml_rpc_call('cmdb.object.update', params)
