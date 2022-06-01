
import random


# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If yes or y, program continues
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no or n, display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response
        # If anything else, repeat question
        else:
            print("Please enter yes or no")


def instructions():
    print("*** How to play ***")
    print()
    print("The rules go here")
    print()
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # i amount is too low / high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print("Please enter a integer between 1 and 10")


# Main routine goes here

played_before = yes_no("Have you played lucky unicorns before? ")
print()
if played_before == "no":
    instructions()

how_much = num_check("How much would you like to play with? ", 0, 10)

# set balance for testing purpose
balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increased # of rounds
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 1 6 and 36
    # user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # the token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    # output
    print("You got a {}. Your balance is "
          "  ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance", balance)
