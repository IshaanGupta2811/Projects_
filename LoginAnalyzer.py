
Failed_Attempts = 0
username = input("Enter Username : ")
Max_attempts = int(input("Enter maximum attempts to check : "))
for i in range(1,Max_attempts+1):
    loginStatus = input("Was the login successful :(Y/n) ")
    

    if(loginStatus == 'n'):
        Failed_Attempts=Failed_Attempts+1

    if(Failed_Attempts==3 and loginStatus=='n'):
        print("*********************************")
        print("Suspicious\n")

    if(Failed_Attempts==5 and loginStatus=='n'):
        print("*********************************")
        print("ALERT: Possible Brute Force Attack\n")
        print("Total Failed Attempts = ",Failed_Attempts )
        break


    if loginStatus == 'Y' :
        print("Login Successful")
        break
print("Username : ",username)
print("Total Failed Attempts = ",Failed_Attempts )
         