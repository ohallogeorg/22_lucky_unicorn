# Function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask user if they have played before
        response = input(question).lower().strip()

        # If yes or y, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If no or n, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")


# Main routine goes here ...
show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))
