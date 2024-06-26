# /usr/bin/python

from idoit_scaleup import createApiCalls, consts

import json

config_file = 'idoit.json'

OBJ_ID = 21096

f = open(config_file)
cfg = json.load(f)
idoit_apis = createApiCalls(cfg)
api = idoit_apis[consts.C__CATS__NET]
api.set_debug_mode()
rtn=api.read_categories(OBJ_ID)
print(json.dumps(rtn))
