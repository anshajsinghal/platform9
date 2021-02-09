class VmMachines(object):
    def __init__(self, name, ip, username, password, os, checkedout=False, clientip=""):
        self.name = name
        self.ip = ip
        self.username = username
        self.password = password
        self.os = os
        self.checkedout = checkedout
        self.clientip = clientip
