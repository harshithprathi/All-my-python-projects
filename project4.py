known_users = ["harshit", "bobby", "sai", "srinu", "avinash"]
while True:
    print("Hi, My name is Travis")
    name = input("what is your name ? : ")
    if name in known_users:
        print("Hello {}".format(name))
        remove=input("Would you like to be removed from system (y/n)?:").strip().lower()
        if remove =="y":
            known_users.remove(name)
            print("Your name has been removed")
        elif remove == "n":
            print("Ok, you are in")
    else :
        print("Sorry I don't think I have met you yet {}".format(name))
        add = input("Would you like to be added to the system (y/n)? :").strip().lower()
        if add == "y":
            known_users.append(name)
            print("Welcome, you are now added to the system")
        elif add == "n":
            print("No worries, see you around!")

