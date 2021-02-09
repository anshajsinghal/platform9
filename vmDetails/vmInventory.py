import json
import os

from common.commonOperations import VmOperations
from vmDetails.vmMachines import VmMachines


class VmInventory(object):
    all_vms = []
    dump_file= "vminventory.json"

    @staticmethod
    def save_dump():
        with open(VmInventory.dump_file, "w+") as file:
            VmInventory.all_vms_json = []
            for vm in VmInventory.all_vms:
                VmInventory.all_vms_json.append(
                    {
                        "name": vm.name,
                        "ip": vm.ip,
                        "username": vm.username,
                        "password": vm.password,
                        "os": vm.os,
                        "checkedout": vm.checkedout,
                        "clientip": vm.clientip
                    }
                )
            json.dump(VmInventory.all_vms_json, file)

    @staticmethod
    def add_vm_to_inventory(name, ip, username, password, os):
        VmInventory.load_dump()
        for vm in VmInventory.all_vms:
            if name == vm.name:
                raise Exception("VM with name {} already exists".format(name))
            elif ip == vm.ip:
                raise Exception("VM with IP {} already exists".format(ip))

        new_vm = VmMachines(name, ip, username, password, os)
        VmInventory.all_vms.append(new_vm)
        VmInventory.save_dump()

    @staticmethod
    def remove_vm_from_inventory(name_or_ip):
        VmInventory.load_dump()
        for vm in VmInventory.all_vms:
            if name_or_ip == vm.name or name_or_ip == vm.ip:
                VmInventory.all_vms.remove(vm)
                VmInventory.save_dump()

    @staticmethod
    def load_dump():
        with open(VmInventory.dump_file, "r") as file:
            VmInventory.all_vms_json = json.loads(str(file.read()))
        for vm in VmInventory.all_vms_json:
            new_vm = VmMachines(vm["name"], vm["ip"], vm["username"], vm["password"], vm["os"], vm["checkedout"], vm["clientip"])
            VmInventory.all_vms.append(new_vm)

    @staticmethod
    def print_vms():
        if len(VmInventory.all_vms<1):
            print("No VMs in inventory")
        else:
            for vm in VmInventory.all_vms:
                print("{name}, {ip}, {os}, {checkedout}".format(
                    name=vm.name, ip=vm.ip, os=vm.os, checkedout=vm.checkedout)
                )

    @staticmethod
    def get_available_vm(clientIP):
        VmInventory.load_dump()
        for vm in VmInventory.all_vms:
            if vm.checkedout == False:
                vm.checkedout = True
                vm.clientip = clientIP
                VmInventory.save_dump()
                return vm
        raise Exception("Sorry! No VM available for checkout. Please try after some time.")

    @staticmethod
    def release_vm_back_to_available(ip, clientIP):
        VmInventory.load_dump()
        for vm in VmInventory.all_vms:
            if ip == vm.ip and clientIP == vm.clientip:
                VmOperations(vm.ip, vm.username, vm.password).exec_command_on_vm("rm -rf /tmp/*")
                vm.checkedout = False
                vm.clientip = ""
                VmInventory.save_dump()
                print("VM with IP {} successfully added back to available VMs".format(vm.ip))
                return
        else:
            print("There is no VM with IP {} or you are not authorized to perform this operation".format(ip))
