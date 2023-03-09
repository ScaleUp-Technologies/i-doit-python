#/usr/bin/python

from idoit_scaleup import createApiCalls,consts
from pprint import pprint
from urllib.parse import urlparse
import json
import re
config_file='idoit.json'

f=open(config_file)
cfg=json.load(f)
f.close()

idoit_apis=createApiCalls(cfg)
layer2_api=idoit_apis[consts.C__CATS__LAYER2_NET]
up=urlparse(cfg['jrpc_url'])
idoit_hostname=up.hostname
objects=idoit_apis[consts.C__OBJTYPE__LAYER2_NET].get_all()
vlans={}
for obj in objects:
    if obj['cmdb_status']==6:
        m=re.match(r'^.*\[(.*)\]$', obj['title'])
        if m:
            vlan=m.group(1)
#            print("vlan: %s" % vlan)
            if not vlan in vlans:
                vlans[vlan]=[]
            vlans[vlan].append(obj)
        else:
            pprint(obj)
            print(obj['id'])
            print(obj['title'])
    else:
        pprint(obj)
for vlan in sorted(vlans.keys()):
    if len(vlans[vlan])>1:
        print('*  **%s**' % vlan)
        for ele in vlans[vlan]:
            print("  * %s Layer2: https://%s/?objID=%s" %( ele['title'], idoit_hostname, ele['id']))
            cats2=layer2_api.read_category(int(ele['id']))
            for id in cats2['layer3_assignments']:
                print("    * Layer3: https://%s/?objID=%d&catsID=22" % (idoit_hostname, id))
            #   pprint(cats2)