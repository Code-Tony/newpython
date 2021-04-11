#register
# - first name, last name, password, email
# - generating user account


#login
# - account number & password


#bank operations
# - deposit and withdraw

#Initializing the system
import random

database = {} #dictionary

#function to start the program
def init():

    print("\nWelcome to bankPHP \n")

 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("\nYou have selected an invalid option. Kindly retry \n")
        init()

#function if login is retried
def loginretry():
    relogin = int(input("Press 1 to retry login, Press 2 to exit \n"))

    if (relogin == 1):

        print("********* Retry Login ***********")
    
        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                         
        print('\nInvalid account or password \n')
        loginretry()

    if (relogin == 2):
        print("****** Exiting login *******\n\n")
        init()

#function for login
def login():
    
    print("\n ********* Login ***********\n")

    accountNumberFromUser = int(input("What is your account number? \n\n"))
    password = input("\nWhat is your password \n\n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                        
    print('\n Invalid account or password')
    loginretry()
    

#function for registration
def register():

    print("\n ****** Register *******\n")

    email = input("\nWhat is your email address? \n\n")
    first_name = input("\nWhat is your first name? \n\n")
    last_name = input("\nWhat is your last name? \n\n")
    password = input("\nCreate a password for yourself \n")

    accountNumber = generationAccountNumber()
    database[accountNumber] = [ first_name, last_name, email, password ]

    print("\nYour Account Has been created \n")
    print(" === ==== ===== ====== ===== ==== ===")
    print("  Your account number is: %d" % accountNumber)
    print("  Make sure you keep it safe")
    print(" === ==== ===== ====== ===== ==== ===")
    login()

#function for general banking operations after successful login
def bankOperation(user):

    print("\n Welcome, %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("\nWhat would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    else:
      
        print("\nInvalid option selected!")
        print("\nRetry \n")
        bankOperation(user)

#function for withdrawal
def withdrawalOperation():
    amountToWithdraw = int(input("\nHow much would you like to withdraw? \n"))
    print("\nPlease, take your cash of", amountToWithdraw, "NGN")
    
    withdrawAgain = int(input("\nPress 1 (to withdraw again) or 2 (to close withdrawal). Note: Invalid response will log you out!\n"))

    if (withdrawAgain == 1):
        withdrawalOperation()

    elif (withdrawAgain == 2):
        logout()

    else:
        print("\nInvalid response. Kindly relogin \n")
        logout()

#function for deposit
def depositOperation():
    amountToDeposit = int(input("\nHow much would you like to deposit? \n"))
    print("\nYour new currect balance is ", amountToDeposit, "NGN\n")

    depositAgain = int(input("\nPress 1 (to deposit again) or 2 (to close deposit). Note: Invalid response will log you out! \n"))

    if (depositAgain == 1):
        depositOperation()

    elif (depositAgain == 2):
        logout()

    else:
        print("\nInvalid response. Kindly relogin \n")
        logout()

#function for account generation
def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

#function for logout
def logout():
    print("\nThank you for banking with us. \n" "You may login for further transactions")
    login()

#function to exit program
def exit():
    init()


#### START PROGRAM #####

init()