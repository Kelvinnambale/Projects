username = input("Enter your username: ")
correct_passwd = "admin123"
password_attempts = 0
max_attempts = 3

while password_attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_passwd:
        print("Welcome!!!...")
        
    else:    
        password_attempts +=1
        print("Incorrect password")


print("Too many failed attemts, Please contact the admin")
    
