def sign_up():
    print("Welcome to the Sign Up Page of the Dijam Voting App")
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    file = open('voters.txt', 'a')
    file.write(name + " " + password + "\n")
    file.close()
    sign_in()


def sign_in():
    print("Welcome to the Sign In Page of the Dijam Voting App")
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    file = open('voters.txt', 'r')
    for user in file:
        username, user_password = user.split()
        if username == name and user_password == password:
            print("Sign in Complete")
            return name
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
    print()


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
        if position in position_dict.keys():
            position_dict[position].append(name)
        else:
            print(f"Position {position} is not available at the moment")
    print(position_dict)
    candidates.close()
    return position_dict


def voting_logic():
    candidate = getContestants()
    j = 0
    q = {}
    i = 0
    for item in candidate:
        for no_of_candidates in candidate[item]:
            q[item, no_of_candidates] = 0
            i += 1

    for specific in candidate:
        if len(candidate[specific]) != 0:
            print("We have " + str(len(candidate[specific])) + " people contesting for this position")
            i = 0
            for people in candidate[specific]:
                print("Enter " + str(i + 1) + " to vote for " + people)
                i += 1
            try:
                vote = int(input("Enter your vote here: "))

                if vote <= len(candidate[specific]) and len(candidate[specific]) != 0:
                    q[specific, candidate[specific][vote - 1]] += 1
                else:
                    print("wrong input. Vote is nullified")
            except ValueError:
                print("Number not entered. Vote nullified")

       
        else:
            print("No candidate for the position " + specific)
    return q


def store_result():
    name = sign_in()
    q = voting_logic()
    results = open('resukt', 'a')
    i = 0
    results.write("This is how " + name + " voted\n")
    for item in q:
        result = q[item]
        results.write(item[0] + ' ' + str(item[1]) + ' ' + str(result) + " votes")
        results.write('\n')
    results.close()


store_result()
