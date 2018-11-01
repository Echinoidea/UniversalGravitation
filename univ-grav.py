import math

class Mass:
	m = 0.0
	posX = 0.0
	posY = 0.0
	
	def __init__(self, m, posX, posY):
		self.m = m
		self.posX = posX
		self.posY = posY
	
	def get_m(self):
		return self.m
		
	def get_posX(self):
		return self.posX
		
	def get_posY(self):
		return self.posY


# Request user input and instantiate a Mass
m1 = input("Enter the mass of the first mass (kg): ")
x1 = input("Enter the x-coordinate of the first mass: ")
y1 = input("Enter the y-coordinate of the first mass: ")

mass1 = Mass(m1, x1, y1)

print("------------------------------------------")

m2 = input("Enter the mass of the second mass (kg): ")
x2 = input("Enter the x-coordinate of the second mass: ")
y2 = input("Enter the y-coordinate of the second mass: ")

mass2 = Mass(m2, x2, y2)

print("------------------------------------------")

# Gravitational constant (in newtons)
G = 6.67 * 10 ** -11

def calc_distance(m1, m2):
	return math.sqrt((m1.get_posX() - m2.get_posX()) ** 2 + (m1.get_posY() - m2.get_posY()))

def calc_force(m1, m2):
	return G * ((m1.get_m() * m2.get_m()) / calc_distance(m1, m2) ** 2)

def calc_vf(m1, m2):
	return math.sqrt(2 * calc_force(m1, m2) * calc_distance(m1, m2))

def calc_totalTime(m1, m2):
	return get_vf(m1, m2) / calc_force(m1, m2)

# Distance between mass1 and mass2
r = calc_distance(mass1, mass2)

# Gravitational force between mass1 and mass2
fG = calc_force(mass1, mass2)

# Time until mass1 and mass2 collide (in seconds)
totalTime = calc_totalTime(mass1, mass2)

print("DISTANCE: {} METERS\nFORCE: {} NEWTONS\nTIME: {}\n".format(r, fG, totalTime))

# End the program
input("Press 'Enter' to exit...")
