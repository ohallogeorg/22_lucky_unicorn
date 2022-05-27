
# Functions go here

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

how_much = num_check("How much would you ike to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
