def sign_up():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    file = open('voters.txt', 'a')
    file.write(name + " " + password + "\n")
    file.close()
    sign_in()


def sign_in():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    file = open('voters.txt', 'r')
    for user in file:
        username, user_password = user.split()
        if username == name and user_password == password:
            print("Sign in Complete")
            return
    print("User not found!!! Register Now!")
    sign_up()


# sign_up()
# sign_in()


def votePage():
    print("Welcome to the Voting Page")
    Postions = ["1: President", "2: Vice President", "3: General Secretary", "4: Treasurer", "5: Sports Director"]
    print("Here are the positions available for contest")
    for position in Postions:
        print(position)
    print


def getContestants():
    position_dict = {
        "President": [],
        "VicePresident": [],
        "GeneralSecretary": [],
        "Treasurer": [],
        "AGS": [],
        "Sports": [],
    }
    candidates = open('candidates.txt', 'r')
    for candidate in candidates:
        name, position = candidate.split()
        if position == "President":
            position_dict["President"].append(name)
        elif position == "VicePresident":
            position_dict["VicePresident"].append(name)
        elif position == "GeneralSecretary":
            position_dict["GeneralSecretary"].append(name)
        elif position == "Treasurer":
            position_dict["Treasurer"].append(name)
        elif position == "AGS":
            position_dict["AGS"].append(name)
        elif position == "Sports":
            position_dict["Sports"].append(name)
        else:
            print(f"Position {position} is not available at the moment")
    print(position_dict)
    return position_dict


def voting_logic():
    candidate = getContestants()
    j = 0

    for item in candidate:
        if len(candidate[item]) > j:
            j = len(candidate[item])
    q = {}
    #q[0,0] = 5

    for specific in candidate:
        if specific == "President":
            print("We have " + str(len(candidate[specific])) + " people contesting for this position")
            i = 0
            for people in candidate[specific]:
                print("Enter " + str(i+1) + " to vote for " + people)
                q[0, i] = 0
                i += 1
            vote = int(input("Enter your vote here: "))
            q[0,vote-1] += 1
            #print(q)

        if specific == "VicePresident":
            print("We have " + str(len(candidate[specific])) + " people contesting for this position")
            i = 0
            for people in candidate[specific]:
                print("Enter " + str(i+1) + " to vote for " + people)
                q[1, i] = 0
                i += 1
            vote = int(input("Enter your vote here: "))
            q[1,vote-1] += 1
           # print(q)


        if specific == "GeneralSecretary":
            print("We have " + str(len(candidate[specific])) + " people contesting for this position")
            i = 0
            for people in candidate[specific]:
                print("Enter " + str(i+1) + " to vote for " + people)
                q[2, i] = 0
                i += 1
            vote = int(input("Enter your vote here: "))
            q[2,vote-1] += 1
            #print(q)

        if specific == "Treasurer":
            print("We have " + str(len(candidate[specific])) + " people contesting for this position")
            i = 0
            for people in candidate[specific]:
                print("Enter " + str(i+1) + " to vote for " + people)
                q[3, i] = 0
                i += 1
            vote = int(input("Enter your vote here: "))
            q[3,vote-1] += 1
            #print(q)
    print(q)


voting_logic()
