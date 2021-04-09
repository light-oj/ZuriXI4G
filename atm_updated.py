### Improve on the your ATM mockup from last course

# 1. Use functions
# 2. Include register and login
# 3. Generate account number
# 4. Any other improvement you can think of (extra point)


#register
# - first name, last name, password, email
# - generate user account number and balance


#login
# - account number & password

#Initializing the system
import random
from datetime import datetime
now = datetime.now()

database = {'2345': ['ade', 'ojo', 'ojo@email.com', '1234', 400000],} 

def main():

    print("Welcome to Pi-Bank")

    haveAccount = int(input("Do you have an account with us? \n 1. Yes \n 2. No \n 3. Exit \n"))

    if (haveAccount == 1):
        login()

    elif (haveAccount == 2):
        register()

    elif (haveAccount == 3):
        exit()

    else:
        print("You have selected an invalid option")
        main()

def login():
    print("********* LOGIN **********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("Enter your password \n")

    for accountNumber,userDetails in database.items():
        if (int(accountNumber) == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print("Invalid account or password")
                login()

def register():

    print("********* REGISTER **********")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("Enter your email address \n")
    password = input("Create a password. \n")

    accountNumber = generateAccountNumber()

    accountBalance = generateAccountBalance()

    database[accountNumber] = [first_name, last_name, email, password, accountBalance]

    print("Your account has been created")
    print("== ==== ====== ====== ==== ==\n")
    print("Your account number is: %d" % accountNumber)
    print("Your dummy opening account balance is: %d" % accountBalance)
    print("Make sure you keep it safe")
    print("\n== ==== ====== ====== ==== ==")

    login()

def bankOperation(user):

    print("Welcome %s %s " % (user[0].upper(), user[1].upper()))
    print("-- {} -- {} --".format(now.strftime("%d %b %y"), now.strftime("%I:%M %p")))

    selectedOption = int(input("What would you like to do? \n ** 1. Deposit \n ** 2. Withdrawal \n ** 3. Check balance \n ** 4. Complaint \n ** 5. Logout \n ** 6. Exit\n"))

    if (selectedOption == 1):
        depositOperation(user)

    elif (selectedOption == 2):
        withdrawalOperation(user)

    elif (selectedOption == 3):
        checkBalanceOperation(user)

    elif (selectedOption == 4):
        complaint(user)

    elif (selectedOption == 5):
        logout()

    elif (selectedOption == 6):
        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)

def checkBalanceOperation(user):
    print("Your account balance is: " + str(user[4]))
    tryAgainOrDone(user)

def depositOperation(user):
    response = int(input("How much would you like to deposit? \n"))
    user[4] += response
    print("****** CASH RECEIVED ****** \nYour new balance is : " + str(user[4]))
    print("Thank you for banking with us.")
    tryAgainOrDone(user)

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def generateAccountBalance():
    return random.randrange(100000, 9999999)

def tryAgainOrDone(user):
    response = int(input("Would you like to perform another transaction? \n ** 1. Yes \n ** 2. No\n"))
    if (response == 1):
        bankOperation(user)
    elif (response == 2):
        print("Thank you")
        print("Goodbye!.....")
    else:
        print("Invalid option selected")
        tryAgainOrDone(user)

def complaint(user):
    response = input("What issue will you like to report? ")
    print("= == === Thank you, {} {}. === == = \n  Your complaint has been received.".format(user[0].upper(), user[1].upper()))
    tryAgainOrDone(user)

def logout():
    login()

def withdrawalOperation(user):
    response = int(input("How much would you like to withdraw?  \n ** 1. 1000    ** 4. 5000 \n ** 2. 2000    ** 5. 10000 \n ** 3. 3000    ** 6. Others\n"))
    if (response == 1):
        user[4] -= 1000
    elif (response == 2):
        user[4] -= 2000
    elif (response == 3):
        user[4] -= 3000
    elif (response == 4):
        user[4] -= 5000
    elif (response == 5):
        user[4] -= 10000
    elif (response == 6):
        response = int(input("Enter amount:  "))
        if (response > user[4]):
            print("Insufficient Balance")
            tryAgainOrDone(user)
        user[4] -= response
    else:
        print("Invalid option selected")
        withdrawalOperation(user)

    print("Take your cash.")
    tryAgainOrDone(user)

##### Pi-Bank System #####
main()