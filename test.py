from array import *
loginTemp = ["admin","user1","1234"]
print("Welcome to the Batty Boys Movie Ticket System")
exit = 0
login = 0

while exit != 1:
    print("Please Enter Command (type help for info)")
    command = input()
    if command =="exit":
        exit = 1
    if command == "help":
        if login == 0:
            print("login = login to the system \n exit = exit the system")
        else:
            print("logout = logout of the system \n buy = buy movie tickets \n sell = sell movie tickets ")
    if command == "login":
        if login != 1:
            print("Enter UserName")
            username = input()
            found = 0
            for name in loginTemp:
                if name == username:
                   found = 1
            if found == 1:
                print("Logged in Successfully")
                login = 1
            else:
                print("User not found on System")   
        else:
            print("Already Logged in")


