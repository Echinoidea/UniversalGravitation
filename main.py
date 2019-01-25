"""
Created by Gabriel Hooks
2018-10-21
------------------------
Simulates gravitational force and attraction between two masses in a 2D vacuum.
Each calculation is one second until the masses collide.
"""

import math
import time

# The Mass object has a mass (kg) and an x/y position.
class Mass:
	m = 0.0	 # The mass (kg) of this object.
	pos_x = 0.0 # The x coordinate of this object.
	pos_y = 0.0 # The y coordinate of this object.

	def __init__(self, m, posX, posY):
		self.m = m
		self.pos_x = posX
		self.pos_y = posY

	@property
	def get_m(self):
		return self.m

	@property
	def get_pos_x(self):
		return self.pos_x

	@property
	def get_pos_y(self):
		return self.pos_y


# Request user input and instantiate a Mass object.
m = float(input("Enter the mass of the first mass (kg): "))
x = float(input("Enter the x-coordinate of the first mass: "))
y = float(input("Enter the y-coordinate of the first mass: "))

# Create the first Mass.
mass1 = Mass(m, x, y)

# Add some pretty lines.
print("------------------------------------------")

# Request user input and instantiate a Mass object.
m = float(input("Enter the mass of the second mass (kg): "))
x = float(input("Enter the x-coordinate of the second mass: "))
y = float(input("Enter the y-coordinate of the second mass: "))

# Create the second Mass.
mass2 = Mass(m, x, y)

# Add some pretty lines.
print("------------------------------------------")

# Gravitational constant (in newtons)
G = 6.67 * 10 ** -11

# Calculate the distance between the two Masses positions.
def calc_distance(m1, m2):
	return math.sqrt(((m1.get_pos_x - m2.get_pos_x) ** 2) + ((m1.get_pos_y - m2.get_pos_y) ** 2))

# Calculate the gravitational force between the two Masses at the current instance.
def calc_force(m1, m2, r):
	return G * ((m1.get_m * m2.get_m) / r ** 2)

# The distance between mass1 and mass2 in meters.
r = calc_distance(mass1, mass2)

# Gravitational force between mass1 and mass2 in newtons.
f_g = calc_force(mass1, mass2, calc_distance(mass1, mass2))

# While the two Masses have NOT collided...
while r > 0:
	# Print out the current calculations.
	print("DISTANCE (M): {}\n   FORCE (N): {}\n".format(r, f_g))
	# Subtract the distance between the two Masses for this instance.
	r -= calc_force(mass1, mass2, r)
	# Calculate the NEW gravitational force between the two Masses.
	f_g = calc_force(mass1, mass2, r)
	# Pause the script for 0.25 seconds until looping again.
	time.sleep(0.25)

# Wait for the user to press ENTER to end the script.
input("")
