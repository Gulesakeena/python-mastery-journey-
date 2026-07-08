'''Login Validation System

Ask the user:

Username:
Password:

Rules:

Username:

Not empty

Password:

At least 8 characters

If valid:

Login Successful

Otherwise:

Display which rule failed.'''

Username = input("Enter username : ")
Password = input("Enter password : ")
if Username != "" and len(Password) >= 8:
    print("Login Successful")
else:
    print("Must enter username and at least 8 character password")
    
    

