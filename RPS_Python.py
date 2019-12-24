import random


def rps():

    play_again = True
    random_number = random.randint(1, 3)
    print(random_number)
    while play_again:
        if random_number == 1:
            comp = "R"
        elif random_number == 2:
            comp = "P"
        else:
            comp = "S"

        user = input("Your turn!\n")

        while user.upper() != "R" and user.upper() != "P" and user.upper() != "S":
            user = input('Please enter "R" for Rock, "P" for Paper, "S" for scissors.\n')

        if user.upper() == comp:
            print("Drew")
        elif (user.upper() == "R" and comp == "S") or\
                (user.upper() == "S" and comp == "P") or\
                (user.upper() == "P" and comp == "R"):
            print("Congrats. You won!")
        else:
            print("Computer won!")

        play_again = input("Do you want play again? Please enter 'YES' or 'Y' for yes or something else for no.\n")

        if play_again.upper() != "Y" and play_again.title() != "Yes":
            play_again = False

    print("Game over! Thank you.")


rps()
