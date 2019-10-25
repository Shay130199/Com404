# Read in user data
print("What is your name?")
name = str( input() )

print("What is your age?")
age = int( input() )

print("What is your weight?")
weight = float( input() )

print("What is your height?")
height = float( input() )

# Calculate bmi
bmi = weight / (height * height)

# Display result
print(name, "your bmi is", bmi)
