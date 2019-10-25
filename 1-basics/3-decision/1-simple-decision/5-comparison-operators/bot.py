# Read in user's first number
print("Please enter first number")
first_number = float(input())

# Read in user's second number
print("Please enter second number")
second_number = float(input())

# Work out which number is bigger
if (first_number < second_number):
    print("\nThe second number is greater.")
elif (first_number > second_number):
    print("\nThe first number is greater.")
else:
    print("\nBoth numbers are equal.")
