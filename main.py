def sign_up():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    file = open('voters.txt','a')
    file.write(name  + " " + password + "\n")
    file.close()
    sign_in()

def sign_in():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    file = open('voters.txt','r')
    for user in file:
        username, user_password = user.split()
        if username == name and user_password == password:
            print("Sign in Complete")
            return
    print("User not found!!! Register Now!")
    sign_up()


#sign_up()
#sign_in()


def votePage():
    print("Welcome to the Voting Page")
    Postions = ["1: President", "2: Vice President", "3: General Secretary", "4: Treasurer", "5: Sports Director"]
    print("Here are the positions available for contest")
    for position in Postions:
        print(position)
    print


votePage()