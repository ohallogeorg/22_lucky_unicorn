# set balance for testing purpose
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increased # of rounds
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    print("Balance: ", balance)
    print()


    if balance < 1:
        # If balance is to low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance", balance)
