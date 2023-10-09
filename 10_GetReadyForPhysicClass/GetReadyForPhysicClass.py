# Project: Getting Ready for Physics Class

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# TURN UP THE TEMPERATURE
# Convert fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Convert celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp) * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# USE THE FORCE
# return mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("\nThe GE train supplies {0} Newtons of force.".format(train_force))

# return the mass times light speed (c) squared
# E = Mc^2
def get_energy(mass, c=3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies {0} Joules.".format(bomb_energy))

# DO THE WORK
# calculate Work = (Ma)*d
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("\nThe GE train does {0} Joules of work over {1} meters.".format(train_work, train_distance))
