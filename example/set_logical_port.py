# /usr/bin/python

from idoit_scaleup import createApiCalls, consts

import json

config_file = 'idoit.json'

OBJ_ID = 4005

f = open(config_file)
cfg = json.load(f)
f.close()
idoit_apis = createApiCalls(cfg)
api = idoit_apis[consts.C__CATG__NETWORK_LOG_PORT]
api.set_debug_mode()
data = {
    'title': 'bond1',
    'mac': 'C8:1F:66:CA:29:52',
    'id': 6,
    'port_type': 1,
    'ports': [7490, 9188]
}
cats = api.update_category(OBJ_ID, data)

data = {
    'title': 'mgm0',
    'id': 7,
    'parent': 6,
    'net': [12619],
}
cats = api.update_category(OBJ_ID, data)

print(json.dumps(cats))
print('----------------')
api.set_debug_mode(False)
cats = api.read_categories(OBJ_ID)
for cat in cats:
    # if cat['id']==6:
    print(json.dumps(cat))
