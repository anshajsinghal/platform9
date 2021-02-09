***ClientOperation***

1. To checkout a VM, run following command:
    
    python enduser.py checkout <your machine IP>
    
2. To checkin a VM:

     python enduser.py checkin <VM IP> <your machine IP>
     
Note : If the IP of the checkin user is different to the IP of checkout user for a VM, then checkin will not be allowed.


***AdminOperations***

1. To add a VM in inventory run below command and follow instructions:

    python adminuser.py addvm

2. To remove a VM from VM inventory:

    python adminuser.py removevm
    
3. To clean a VM:

    python adminuser.py cleanvm
    
4. After restart the machine, to load the state of VMs:

    python adminuser.py loadvm
    
Note : Currently, every command is run as a new command and it considers as the system is restarted, 
so we dont need to "loadvm" as of now. All the actions are written in a way to load the inventory status first.
