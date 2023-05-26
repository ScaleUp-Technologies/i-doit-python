# /usr/bin/python

from idoit_scaleup import createApiCalls, consts

import json

config_file = 'idoit.json'

OBJ_ID = 3115

f = open(config_file)
cfg = json.load(f)
f.close()
idoit_apis = createApiCalls(cfg)
api = idoit_apis[consts.C__CATG__NETWORK_LOG_PORT]
api.set_debug_mode()
data = {
    'title': 'mgm0',
    'id': 114,
    'active': 1,
    'port_type': 1,
    'ports': [],
    'addresses': [256],
}
cats = api.update_category(OBJ_ID, data)


print(json.dumps(cats))
print('----------------')
api.set_debug_mode(False)
cats = api.read_categories(OBJ_ID)
for cat in cats:
    print(json.dumps(cat))
