from vmDetails.vmInventory import VmInventory


class ClientOperations(object):
    def __init__(self):
        pass

    def checkout_vm(self, clientIP):
        vm = VmInventory.get_available_vm(clientIP)
        print("{name}, {ip}, {os}".format(name=vm.name, ip=vm.ip, os=vm.os))

    def ckeckin_vm(self, ip, clientIP):
       VmInventory.release_vm_back_to_available(ip, clientIP)
