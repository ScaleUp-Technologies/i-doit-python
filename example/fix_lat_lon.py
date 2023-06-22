# /usr/bin/python

from idoit_scaleup import createApiCalls, consts, conditional_read
import json

config_file = 'idoit_live.json'


def fix_lat(obj_id, loc_api):
    loc = loc_api.read_category(obj_id)
    new_loc = {}
    for fieldname in ['parent', 'id', 'insertion', 'option', 'pos', 'latitude', 'longitude', 'description', 'snmp_syslocation']:
        if fieldname in loc.keys():
            new_loc[fieldname] = loc[fieldname]

    if new_loc['latitude'] == 0.0 and new_loc['longitude'] == 0.0:
        new_loc['latitude'] = None
        new_loc['longitude'] = None
        if 'pos' in new_loc.keys() and ('insertion' not in new_loc.keys() or new_loc['insertion'] is None):
            del (new_loc['pos'])
        rtn = loc_api.update_category(obj_id, new_loc)
        if rtn is None:
            print(json.dumps(loc))
            print(json.dumps(new_loc))
            loc = loc_api.read_category(obj_id)
            print(json.dumps(loc))
        else:
            print('Update')
        # print(json.dumps(loc))
        # print(json.dumps(new_loc))


f = open(config_file)
cfg = json.load(f)
f.close()

search = conditional_read(cfg)
search.add_search_param(consts.C__CATG__LOCATION, 'latitude', 0.0)
search.add_search_param(consts.C__CATG__LOCATION, 'longitude', 0.0, 'AND')
search_result = search.search()
idoit_apis = createApiCalls(cfg)
print('---------------------------------------------')
print(len(search_result))
print('---------------------------------------------')
for ele in search_result:
    print(ele['id'])
    loc_api = idoit_apis[consts.C__CATG__LOCATION]
    loc_api.set_debug_mode()
    fix_lat(ele['id'], loc_api)


#fix_lat(OBJ_ID, idoit_apis[consts.C__CATG__LOCATION])
