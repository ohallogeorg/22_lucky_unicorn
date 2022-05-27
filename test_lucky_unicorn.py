
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
    print()
    print("*** How to play ***")
    print()
    print("The rules go here")
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


# Main routine goes here ...

played_before = yes_no("Have you played lucky unicorns before? ")
if played_before == "no":
    instructions()

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

print("Program Continues")
