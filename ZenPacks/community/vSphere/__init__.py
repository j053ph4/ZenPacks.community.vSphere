import Globals
import os.path
import sys

# skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
# from Products.CMFCore.DirectoryView import registerDirectory
# if os.path.isdir(skinsDir):
#     registerDirectory(skinsDir, globals())
# 
# libDir = os.path.join(os.path.dirname(__file__), 'lib')
# if os.path.isdir(libDir):
#     sys.path.append(libDir)

# add/remove zproperties

from Products.ZenModel.ZenPack import ZenPackBase

class ZenPack(ZenPackBase):
    "ZenPack Loader that loads zProperties used by ZenAWS"
    packZProperties = [
            ('zVSphereHost', '', 'string'),
            ('zVSpherePort', 443, 'int'),
            ('zVSphereUser', '', 'string'),
            ('zVSpherePassword', '', 'password'),
        ]
    
    def install(self, app):
        ZenPackBase.install(self, app)
        dc = app.dmd.Devices.createOrganizer('/VMWare')
        #dc.setZenProperty('zCollectorPlugins',
        #                    ('zenoss.aws.EC2InstanceMap',))
        #dc.setZenProperty('zPythonClass', 'ZenPacks.zenoss.ZenAWS.EC2Manager')
        #if dc.devices._getOb('EC2Manager', None): return
        #ec2m = dc.createInstance('EC2Manager')
        #ec2m.setPerformanceMonitor('localhost')
