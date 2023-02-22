# /usr/bin/python

from idoit_scaleup import createApiCalls, consts

import json

config_file = 'idoit.json'

OBJ_ID = 4005

f = open(config_file)
cfg = json.load(f)
f.close()
idoit_apis = createApiCalls(cfg)
api = idoit_apis[consts.C__CATG__NETWORK_PORT]
api.set_debug_mode()
data = {
    'title': 'eth2',
    'addresses': [],
    'mac': '90:E2:BA:74:27:DC',
    'id': 9201,
    'interface': 408
}
cats = api.update_category(OBJ_ID, data)
print(json.dumps(cats))
print('----------------')
api.set_debug_mode(False)
cats = api.read_categories(OBJ_ID)
for cat in cats:
    if cat['id'] == 9201:
        print(json.dumps(cat))
