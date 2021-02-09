from vmDetails.vmInventory import VmInventory


class AdminOperations(object):
    def __init__(self):
        pass

    def clean_vm(self, ip):
        VmInventory.release_vm_back_to_available(ip)

    def add_new_vm(self, name, ip, username, password, os):
        VmInventory.add_vm_to_inventory(name, ip, username, password, os)

    def remove_existing_vm(self, name_or_ip):
        VmInventory.remove_vm_from_inventory(name_or_ip)

    def load_vm(self):
        VmInventory.load_dump()
