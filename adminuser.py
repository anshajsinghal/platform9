import sys

from administrator.adminOperations import AdminOperations

if __name__ == "__main__":
    if sys.argv[1] == "addvm":
        name = input("\nPlease enter the name of the vm : ")
        ip = input("\nPlease enter the IP of the vm : ")
        username = input("\nPlease enter the username of the vm : ")
        password = input("\nPlease enter the password of the vm : ")
        os = input("\nPlease enter the OS of the vm : ")
        AdminOperations().add_new_vm(name, ip, username, password, os)
    elif sys.argv[1] == "removevm":
        name_or_ip = input("\nPlease enter the name or IP of the vm : ")
        AdminOperations().remove_existing_vm(name_or_ip)
    elif sys.argv[1] == "cleanvm":
        name_or_ip = input("\nPlease enter the name or IP of the vm : ")
        AdminOperations().clean_vm(name_or_ip)
    elif sys.argv[1] == "loadvm":
        AdminOperations().load_vm()

    else:
        print("This operation is not supported.")