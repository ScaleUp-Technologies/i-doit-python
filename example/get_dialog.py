# /usr/bin/python

from idoit_scaleup import createApiDialogs, consts

import json

config_file = 'idoit.json'

OBJ_ID = 4005

f = open(config_file)
cfg = json.load(f)
f.close()
rtn = createApiDialogs(cfg, consts.C__CATG__IP, 'assigned_port').get_all()
print(json.dumps(rtn))
