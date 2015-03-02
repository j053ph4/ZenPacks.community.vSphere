from Globals import InitializeClass
from Products.ZenModel.Device import Device, manage_createDevice
from Products.ZenModel.Exceptions import DeviceExistsError
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenRelations.RelSchema import *


class vmHost(Device):
    ''''''
    meta_type = portal_type = 'vmHost'
    
    _relations = Device._relations + (
        ('vmcluster', ToOne(ToMany,
            'ZenPacks.community.vSphere.vmCluster.vmCluster',
            'vmhosts',
            ),
        ),                   
        ('vmdatacenter', ToOne(ToMany,
            'ZenPacks.community.vSphere.vmDataCenter.vmDataCenter',
            'vmhosts',
            ),
        ),
        ('vmdatastores', ToMany(ToMany,
            'ZenPacks.community.vSphere.vmDatastore.vmDatastore',
            'vmhosts',
            ),
        ),
        ('vmdatastoreclusters', ToMany(ToMany,
            'ZenPacks.community.vSphere.vmDatastoreCluster.vmDatastoreCluster',
            'vmhosts',
            ),
        ),
        ('vmfolders', ToMany(ToMany,
            'ZenPacks.community.vSphere.vmFolder.vmFolder',
            'vmhosts',
            ),
        ),                    
        ('vmguests', ToMany(ToOne,
            'ZenPacks.community.vSphere.vmGuest.vmGuest',
            'vmhost',
            ),
        ),                
        ('vmnetworks', ToMany(ToMany,
            'ZenPacks.community.vSphere.vmNetwork.vmNetwork',
            'vmhosts',
            ),
        ),
         ('vmresourcepools', ToMany(ToMany,
            'ZenPacks.community.vSphere.vmResourcePool.vmResourcePool',
            'vmhosts',
            ),
        ),
    )

InitializeClass(vmHost)
