# Functions go here


# Main routine goes here

error = "Please enter a whole number between 1 and 10"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("How much would you like to play with? "))
        # i amount is too low / high give
        if 0 < response <= 10:
            print("You asked to play "
                  "with ${}".format(response))

            # output an error
        else:
            print("Number is outside amount allowed")

    except ValueError:
        print("Please enter a integer between 1 and 10")
