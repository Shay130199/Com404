# Read direction from user
print("Towards which direction should I paint (up, down, left or right)")
direction = input()

# Determine direction
message = "\nI am painting in the "

if (direction == "up"):
    message += "upward"
elif (direction == "down"):
    message += "downward"
elif (direction == "left"):
    message += "leftward"
elif (direction == "right"):
    message += "rightward"

message += "direction"

# Display message
print(message)


# We can simplify the above code to display a message as follows:
#
# print("\nI am painting in the " + direction + "ward direction")
#
# However, our aim was to practice writing an if...elif...else statement