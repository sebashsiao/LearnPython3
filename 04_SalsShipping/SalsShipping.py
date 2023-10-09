# Project 004: SALS'S SHIPPING

#weight = 4.8
weight = 41.5

# Ground shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

# Ground shipping Premium
cost_ground_p = 125.0

print(f'Ground shipping cost: $ {cost_ground}')
print(f'Premium Ground shipping cost: $ {cost_ground_p}')

#weight = 1.5

# Drone shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.75

print(f'Drone shipping cost: $ {cost_drone}')
