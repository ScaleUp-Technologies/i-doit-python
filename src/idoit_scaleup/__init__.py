from .object import IDoitObject
from . import consts
from pprint import pprint
from .cat_access import IDoitAccess
from .cat_connector import IDoitConnector
from .cat_cpu import IDoitCpu
from .cat_ip import IDoitIP
from .cat_location import IDoitLocation
from .cat_memory import IDoitMemory
from .cat_network import IDoitNetwork
from .cat_networkport import IDoitNetworkPort
from .cat_power_consumer import IDoitPowerConsumer
from .cat_racktables import Racktables
from .cat_vlan import IDoitVlan
from .category import IDoitCategory
from .conditional_read import IDoitConditionalRead
from .dialog import IDoitDialog
from .search import IDoitSearch
from .cat_storage_device import IDoitStorageDevice
import sys
import inspect

def createApiCall(cfg, category):
    current_module = sys.modules[__name__]
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj):
            if issubclass(obj, IDoitCategory):
                try:
                    found=False
                    found = (obj.CATEGORY == category)
                    if found:
                        return obj(cfg)
                except AttributeError:
                    pass
    if category.startswith('C__OBJTYPE__'):
        return IDoitObject(cfg, category)
    if category.startswith('C__CATS__') or category.startswith('C__CATG__'):
        return IDoitCategory(cfg, category)
    return None


def createApiCalls(cfg):
    rtn = {}
    for varname in consts.__dict__.keys():
        if not (varname in rtn.keys()):
            rtn[varname] = createApiCall(cfg, varname)
    return rtn


def createApiDialogs(cfg, category, field):
    if 'dialogs' not in cfg.keys():
        cfg['dialogs'] = {}
    if category not in cfg['dialogs'].keys():
        cfg['dialogs'][category] = {}
    if field not in cfg['dialogs'][category].keys():
        cfg['dialogs'][category][field] = IDoitDialog(cfg, category, field)
    return cfg['dialogs'][category][field]


def search(cfg):
    return IDoitSearch(cfg)


def conditional_read(cfg):
    return IDoitConditionalRead(cfg)

def get_all_classes():
    rtn=[]
    current_module = sys.modules[__name__]
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj):
            rtn.append(name)
    return rtn
