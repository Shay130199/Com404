import math

# Read radius from user 
print("Please enter radius") 
radius = float( input() )

# Calculate area and circumference 
area = math.pi * (radius * radius)
# Alternatively:
# area = math.pi * (radius ** 2)
# area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius

# Display result
print("Area is", area)
print("Circumference is", circumference)
