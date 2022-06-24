"""Example of looping through all characters in a string."""

user_string: str = input("Give me a string! ")

# The variable i is a common counter 
# varaible name in programming.
# i is short for interation.

i: int = 0

while i < len(user_string):
    print(user_string[i])
    # starting at the end to make sure there is progress 
    i = i + 1

print("Done!")
