"""
Created by Gabriel Hooks
2018-10-21
"""

import math

class Mass:
    m = 0.0
    pos_x = 0.0
    pos_y = 0.0

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


# Request user input and instantiate a Mass
m = float(input("Enter the mass of the first mass (kg): "))
x = float(input("Enter the x-coordinate of the first mass: "))
y = float(input("Enter the y-coordinate of the first mass: "))

mass1 = Mass(m, x, y)

del m
del x
del y

print("------------------------------------------")

m = float(input("Enter the mass of the second mass (kg): "))
x = float(input("Enter the x-coordinate of the second mass: "))
y = float(input("Enter the y-coordinate of the second mass: "))

mass2 = Mass(m, x, y)

del m
del x
del y

print("------------------------------------------")

# Gravitational constant (in newtons)
G = 6.67 * 10 ** -11


def calc_distance(m1, m2):
    return math.sqrt(((m1.get_pos_x - m2.get_pos_x) ** 2) + ((m1.get_pos_y - m2.get_pos_y) ** 2))


def calc_force(m1, m2, r):
    return G * ((m1.get_m * m2.get_m) / r ** 2)


def calc_vf(m1, m2):
    return math.sqrt(2 * calc_force(m1, m2, calc_distance(m1, m2)) * calc_distance(m1, m2))


def calc_total_time(m1, m2):
    return calc_vf(m1, m2) / calc_force(m1, m2, calc_distance(m1, m2))


# Distance between mass1 and mass2
r = calc_distance(mass1, mass2)

# Gravitational force between mass1 and mass2
f_g = calc_force(mass1, mass2, calc_distance(mass1, mass2))

while r > 0:
    print("DISTANCE: {} METERS\n   FORCE: {} NEWTONS\n".format(r, f_g))
    r -= calc_force(mass1, mass2, r)
    f_g = calc_force(mass1, mass2, r)

input("")
