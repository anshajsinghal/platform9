# import paramiko


class VmOperations(object):
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    def exec_command_on_vm(self, command):
        print("I have come to clean VM")
        return

    # def exec_command_on_vm(self, command):
    #     path = self.ip + ":/tmp"
    #     try:
    #         ssh = paramiko.SSHClient()
    #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #         ssh.connect(path, self.port, self.username, self.password)
    #     except:
    #         print("Could not SSH to {}".format(self.host))
    #         return False
    #
    #     stdin, stdout, stderr = ssh.exec_command(command)
    #     ssh.close()
    #
    #     return True
