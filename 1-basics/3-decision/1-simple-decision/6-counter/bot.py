# Ask user to enter 3 numbers
print("Please enter first number")
first_number = int(input())

print("Please enter second number")
second_number = int(input())

print("Please enter third number")
third_number = int(input())

# Work out how many are even and how many are odd
evens = 0
odds = 0

if (first_number % 2 == 0):
    evens += 1
    # or even_count += 1
else:
    odds += 1

if (second_number % 2 == 0):
    evens += 1
    # or even_count += 1
else:
    odds += 1

if (third_number % 2 == 0):
    evens += 1
    # or even_count += 1
else:
    odds += 1

print("\nThere were", evens, "even and", odds, "odd numbers.")
