def sign_in():
    email = "adesokanmajid@gmail.com"
    password = "12345678"
    print("Welcome to the Voting today. Kindly sign in or Press Y to sign up")
    user_email = input("Enter your email or press Y to sign up: ")
    if user_email in "Yy":
        signUp()
        return
    else:
        user_password = input("Enter your password: ")
    if email != user_email or user_password != password:
        print("Email or Password not correct. Retry or SignUp")
        sign_in()
    else:
        print("Welcome to the voting app " + user_email)


def signUp():
    print ("Sign Up page")

sign_in()


