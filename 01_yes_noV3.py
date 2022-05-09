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


# Main routine goes here ...
played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    print("*** How to play ***")
    print()
    print("The rules go here")
