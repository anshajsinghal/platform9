import sys
from client.clientOperations import ClientOperations

if __name__ == "__main__":
    if sys.argv[1] == "checkout":
        try:
            ClientOperations().checkout_vm(sys.argv[2])
        except IndexError:
            print("Please make sure to provide your IP")
    elif sys.argv[1] == "checkin":
        try:
            ClientOperations().ckeckin_vm(sys.argv[2], sys.argv[3])
        except IndexError:
            print("Please make sure to provide all correct details of the VM to checkin along with your IP address.")
    else:
        print("Accepted operations are 'checkin' or 'checkout'.")