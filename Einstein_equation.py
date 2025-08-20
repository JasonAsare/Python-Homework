'''
Einstein equation of energy.
'''

#Speed of light
SPEED_OF_LIGHT = 3.0*10**8
#User can input any integer as mass
mass = int(input("Enter Mass: "))
energy = mass * SPEED_OF_LIGHT ** 2
print(f"Energy:", energy)