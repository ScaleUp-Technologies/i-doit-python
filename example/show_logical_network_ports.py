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
cats = api.read_categories(OBJ_ID)
print(json.dumps(cats))
