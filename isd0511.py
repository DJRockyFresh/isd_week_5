password = "changeme"
userinput = input("Enter your password: ")
tries = 1

while userinput != password:
    print ("Wrong password, try again!")
    userinput = input("Enter your password: ")
    tries = tries + 1

    if userinput == password:
        print ("Welcome back!")
    elif tries > 5:
        print ("Access denied! Reset your password")
        break
print (tries, "Attepmts were taken")



    
    
