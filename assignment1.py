import re

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex,email)

def validate_password(password):
    regex = reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    return re.search(regex, password)

def registration():
    email = input("Enter Email Id: ")
    while not validate_email(email):
        email = input("Invalid email address. Please enter a valid email: ")
    password = input("Enter a password (The password must contain atlease one special character "
                     ", one digit, one uppercase, one lowercase and should be 5 to 16 characters long): ")
    while not validate_password(password):
        password = input("Invalid password. Please enter a valid password: ")

    with open('emailpass.txt', 'a') as file:
        file.write(email + " " + password + "\n")

    print("Account created successfully")

def forget_pass(creds, ind):
    print("\nPress 1 to know your old password.")
    print("press 2 to change password")

    inp = int(input())

    if inp == 1:
        print("\nOld password: ", creds[ind].split(" ")[1])
    elif inp == 2:
        password = input("\nEnter new Password: ")
        while not validate_password(password):
            password = input("Invalid password. Please enter a valid password: ")

        creds[ind] = creds[ind].split(" ")[0] +" "+password
        with open('emailpass.txt', 'w+') as file:
            for cred in creds[:-1]:
                file.write(cred+"\n")

        print("Password Changed Successfully")
    else:
        print("Invalid input")



def login():
    email = input("Enter Email Id: ")
    password = input("Enter password: ")
    file = 0
    try:
        file =  open('emailpass.txt', 'r+')
    except:
        print("file does not exist. Please register some entries.")
        return

    creds = file.read().split("\n")
    for ind, cred in enumerate(creds[:-1]):
        id, pas = cred.split(" ")
        if id == email:
            if pas == password:
                print("Welcome!")
                print("Your Creds are matching.")
                return
            else:
                print("The password you provided is incorrect.")
                inp = input("Forgot password (n/y): ")
                if inp.upper() == 'Y':
                    forget_pass(creds, ind)
                return
    print("The email does not exist.")
    inp = input("Do you want to register? (n/y): ")
    if inp.upper() == 'Y':
        print(end='\n')
        registration()
    file.close()

if __name__ == '__main__':
    print("Press 1 for registration.")
    print("Press 2 for login.")
    inp = int(input())
    print(end="\n")

    if inp == 1:
        registration()
    elif inp == 2:
        login()
    else:
        print("Invalid input")

