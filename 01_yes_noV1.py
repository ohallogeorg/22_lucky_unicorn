# Ask the user if they have played before
show_instructions = input("Have you played this game before? ").lower() .strip()

# If they say yes or y, output 'program continues'
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("display instructions")

# If they say anything else 'Please answer yes / no'
else:
    print("Please answer yes / no")
