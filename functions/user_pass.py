username = "user"
password = "123"

def login():
    a = input("Enter username : ")
    b = input("Enter Password : ")

    if a == username and b == password:
        print("Login Successful")
    else:
        print("Invalid username or password")

        while True:
            print("1. Forgot password")
            print("2. Exit")

            choice = input("Enter your choice (1 or 2) : ")

            if choice == "1":
                forgot_password()
                break

            elif choice == "2":
                print("Exit")
                break

            else:
                print("Invalid choice")


def forgot_password():
    global password

    check_user = input("Enter username : ")

    if check_user == username:
        print("Username is correct")

        new_pass = input("Enter new password : ")
        password = new_pass

        print("Password changed successfully")
    else:
        print("Username is wrong")


login()
