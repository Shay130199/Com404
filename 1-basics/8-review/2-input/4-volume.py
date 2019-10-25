import math 

print("Please enter cylinder or cone")
shape = input() 

print("Please enter radius of the shape")
radius = float(input())

print("Please enter the height of the shape")
height = float(input())

if (shape == "cylinder"):
  volume = math.pi * (radius ** 2) * height 
  print("The volume of the cylinder is", volume)
elif (shape == "cone"):
  volume = (math.pi * (radius ** 2) * height) / 3
  print("The volume of the cone is", volume)
else:
  print("Don't know")
