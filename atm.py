from datetime import datetime
now = datetime.now()
name = input("What is your name? \n")
allowed_names = ["Akolade", "Seyi", "John"]
allowed_password = ["passwordAkolade", "passwordSeyi", "passwordJohn"]
current_balance = 100000

if (name in allowed_names):
    password = input("Enter your password: ")
    userId = allowed_names.index(name)

    if (password == allowed_password[userId]):

        print("Welcome %s" % name)
        print("-- {} -- {} --".format(now.strftime("%d %b %y"), now.strftime("%I:%M %p")))
        print("These are the available options: ")
        print("1. Withdraw")
        print("2. Cash Deposit")
        print("3. Complaint")

        selectedOption = int(input("Please select an option: "))

        if (selectedOption == 1):
            #print("You have selected %s" % selectedOption)
            response = int(input("How much would you like to withdraw? "))
            print("Take your cash")

        elif (selectedOption == 2):
            #print("You have selected %s" % selectedOption)
            response = int(input("How much would you like to deposit? "))
            print("Current balance is :" + str(response + current_balance))

        elif (selectedOption == 3):
            #print("You have selected %s" % selectedOption)
            response = input("What issue will you like to report? ")
            print("Thank you for contacting us")
        
        else:
            print("Invalid option selected, please try again")

    else:
        print("Password Incorrect, please try again")

else:
    print("Name not found, please try again")

