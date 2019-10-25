# ask the user where to look
print("Where should I look?")
place = input()

# determine where the battery is located
if (place == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bedroom_place = input()

    if (bedroom_place == "under the bed"):
        print("Found some shoes but no battery.")
    else:
        print("There is mess but no battery.")
else:
    print("I don't know where that is but I will keep looking.")
