# Ask where forky is
print("Where is Forky?")
direction = input()

# Determine direction
message = "\nWith Bonnie "

if (direction == "With Bonnie"):
    message += "Phew! Bonnie will be happy"
elif (direction == "Running away"):
      message += "Oh no! Bonnie will be upset!" 
elif (direction == "No"):
    message += "Ah! I better look for him."


# Display Message
print(message)