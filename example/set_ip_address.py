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
api.read_categories(OBJ_ID)
api = idoit_apis[consts.C__CATG__IP]
api.set_debug_mode()
data = {
    'id': 11,
    # 'assigned_port': ('7_%s' % consts.C__CATG__NETWORK_LOG_PORT)
    'assigned_port': 'eth0'
}
rtn = api.update_category(OBJ_ID, data)
print(json.dumps(rtn))
print('----------------')
# api.set_debug_mode(False)
# ips=api.read_categories(OBJ_ID)
# for obj in ips:
#    #if cat['id']==6:
#    print(json.dumps(obj))
