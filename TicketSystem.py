#!/usr/bin/python
from array import *

#temporary arrays used as local database for initial prototype testing.
loginTemp = ["admin","user1","1234"]
eventTemp = ["movie", "bumba", "nyeah"]
SellerAndTix = [["ticketmaster",120],["bob",3],["bucktee",7]]

#initial login screen
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  Welcome to the Batty Boys Movie Ticket System")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
exit = 0
login = 0
admin = 0

# Performs user login, and necessary logic
def LoginUser():
    global login
    global admin
    if login == 1:
        print("\n  Already Logged in")
    #when login is 0
    else:
        print("\n  Enter User Name:\n")
        username = input()
        for name in loginTemp:
            if name == username:
                login = 1
                print("\n  Logged in Successfully")
            if username == "admin":
            	admin = 1
        if login == 0:
            print("\n  User not found on System")   
    return

# Buy function where a buyer account may buy tickets to an event.
def Buy():
    print("\n  What event do you want to buy tickets for?\n")
    for eventname in eventTemp:
        print("   - ", eventname)
    event = input()
    found = 0
    #for loop that iterates through current events and checks to see if user's input matches a current event title
    for eventname in eventTemp:
        if eventname == event:
            found = 1
            print("\n  How many tickets will you like to buy? (Max 4 tickets per Sale)\n") #Max tickets constraint applied (4 tickets per sale)
            numoftix = input()
            while int(numoftix) > 4:
                print("\n  Sorry that's too many tickets, try again:\n")
                numoftix = input() #loops back until user enters a number less than 4
            print("\n  Enter the username of the seller:\n")
            buyerfound = 0
            buyerName  =""
            buyerTix = 0
            sellername = input()
            for seller in SellerAndTix: #for loop that checks to see if seller username and valid numberof tickets exists. IF both are found continue; else end transaction;
                if seller[0] == sellername:
                    if seller[1] > int(numoftix):
                        buyerfound = 1
                        buyerName = seller[0]
                        buyerTix  = seller[1]
            if buyerfound == 1:
                print("\n  '" + buyerName + "' has tickets for this price \n  Would u like to purchase \n  (type yes or no):\n")
                buy = input()
                #user inputs if they want to proceed with the transaction or not after looking at the total price.
                if buy == "yes":
                    print("\n  You have successfully purchased the tickets")
                else:
                    print("\n  Transaction cancelled")
            else:
                print("\n  Buyer was not found \n  Transaction Cancelled")
           
    if found == 0:
        print("\n  Sorry that event isn't happening right now")

# Sell function where a seller account may sell tickets to an event.
def Sell():
    print("\n  What event do u want to sell Tickets for\n  ")
    event = input()
    print("\n  Under what name should the tickets be sold from\n  ")
    name = input()
    print("\n  How many tickets do u have avaiable for sale\n  ")
    numoftix = int(input())
    eventTemp.append(event)
    SellerAndTix.append([name,numoftix])
    #Added Seller's username, number of tickets, and event to Event and SellerAndTix Array. 
    print("\n  Tickets are now Officially on Sale\n  ")


#Refund function that allows the admin to add funds back into a buyers account from a seller's account.
def Refund():
    print("\n  Enter buyer for refund\n  ")
    buyer = input()
    print ("\n  Enter seller for refund\n  ")
    seller = input()
    buyerfound = 0
    for user in loginTemp: #search for valid buyer username
        if user == buyer:
            buyerfound = 1
    if buyerfound == 1:
            sellerfound = 0
            for sell in SellerAndTix: #search for valid seller username
                if sell[0] == seller:
                    sellerfound = 1
    else:
        print("\n  User was not found\n ") 
    if sellerfound == 1: #if both are found then refund the amount to buyer.
        print ("\n How many credits to refund?\n ")
        refund = input()
        print ("\n  " + buyer + " was refunded " + refund + " credits from " + seller + "\n")
    else:
        print("\n  Seller was not found\n ")

#Addcredit function that will allow admin account to add credit to any valid account.
def addCredit():
    print("\n  Enter username to add credits to\n")
    username = input()
    userfound = 0
    for user in loginTemp: #search for valid username within data
        if user == username:
            userfound = 1
    if userfound == 1: #if found ask how many credits to add
        print("\n  Enter number of credits to add\n")
        credit = input() #add credits
        print(username + " has been creditted " + credit + " dollars")
    else:
        print("\n  User has not been found")
            
#Create Fucntion that allows admin to create new buyer, seller, or admin accounts.
def Create():
    print("\n  Enter the new account's username:\n")
    username = input()
    print("\n  What type of user is this (admin, buyer, seller):\n")
    accountType = input()
    print("\n  How much credit is in this account?:\n")
    credit = input()
    loginTemp.append(username) #add new account to loginTemp Array.
    print("\n  Successfully created new user: '" + username + "' of Type: '" + accountType + "' with Credit: '" + credit +"'")

#Delete function that allows admin to delete an existing account from the database(array).
def Delete():
	userfound = 0
	print("\n  Enter the account's username that you wish to delete:\n")
	username = input()
	for user in loginTemp:
	    if user == username:
	        userfound = 1
	#if input account exists then delete user (remove user from loginTemp array).
	if userfound == 1:
	   	loginTemp.remove(username)
	else:
		print("\n  User not found")
	print("\n  Successfully deleted user!")


# Displays avaiable commands for users
def help():
    print("\n  Ask and ye shall receive!:\n")
    if login == 0:
        print("  login = login to the system")
        print("  exit = exit the system")
    else:
        print("  logout = logout of the system ")
        print("  buy = buy movie tickets ")
        print("  sell = sell movie tickets ")
        print("  refund = refund a user credits (admin only)")
        print("  add credit = add credit to a users account (admin only)")
        print("  create = creates a new user (admin only)")
        print("  delete = deletes a user's account (admin only)")
    return


#while loop for commands (Main Function)
while exit != 1:
    print("\n  Please Enter Command (type help for info)  \n")
    command = input().lower()
    
    if command =="exit":
        exit = 1

    elif command == "help":
        help()

    elif command == "login":
        LoginUser()

    elif command == "logout":
        #login check
        if login == 0:
            print("\n  Unable to logout due to no account being logged in")
        elif login ==1:
            print("\n  Logged Out Successfully")
            login =0 
    
    elif command == "buy":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1: 
            Buy()

    elif command == "sell":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1:
            Sell()

    elif command == "refund":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1 and admin == 1:
            Refund()
        else:
        	print("\n  You sneaky fool, only admins allowed!")

    elif command == "add credit":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1 and admin == 1:
            addCredit()
        else:
        	print("\n  You sneaky fool, only admins allowed!")

    elif command == "create":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1 and admin == 1:
            Create()
        else:
        	print("\n  You sneaky fool, only admins allowed!")

    elif command == "delete":
        #login check
        if login == 0:
            print("\n  Not logged in yet")
        elif login == 1 and admin == 1:
            Delete()
        else:
        	print("\n  You sneaky fool, only admins allowed!")

    else:
        print("\n  Invalid Command!")