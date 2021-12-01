films = {
    "Rrr":[9,9],
    "Acharya":[15,7],
    "Kgf-2":[18,6],
    "Pushpa":[19,6],
    }
while True:    
    choice = input("Which film you want to watch? : ").strip().title()
    if choice in films:
        age = int(input("What is your age? : ").strip())
        if age>=films[choice][0]:
            num_seats = films[choice][1]
            if num_seats>0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are sold out")
        else:
            print("Sorry you are too young to watch this film")
    else:
        print("Sorry we dont have that film")
