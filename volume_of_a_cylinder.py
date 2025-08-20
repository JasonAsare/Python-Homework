'''
Volume of a cylinder
'''

#Pi
PI = 3.14
#Calculating the radius by user input
radius = int(input("Enter radius: "))
#Calculating the height by user input
height = int(input("Enter the height: "))
volume = PI * radius**2* height
print(f"The volume of the cylinder is", volume)