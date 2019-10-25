import math 

# Read radius from user
print("Please enter radius")
radius = float( input() )

# Calculate area and circumference
area = math.pi * (radius * radius)
# Alternatively:
# area = math.pi * (radius ** 2)
# area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius

# Display the result
print("Area is", round(area, 2))
print("Circumference is", round(circumference, 2))

