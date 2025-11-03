import os
from twisted.application import service
from buildbot.master import BuildMaster

basedir = os.path.dirname(__file__)
configfile = "master.cfg"

application = service.Application("buildbot")
m = BuildMaster(basedir, configfile)
m.setServiceParent(application)
