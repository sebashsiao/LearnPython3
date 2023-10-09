# Project 007: Icecream Shop Scoops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# Three branches names
branch = ["Scoopcademy", "Gilberts Creamery", "Manny’s Scoop Shop"]

scoops_sold = 0

# Loop of each different location's data
for n, location in enumerate(sales_data):
  print(f'Location {sales_data.index(location)+1} \'{branch[n].upper()}\': {sum(location)} scoops sold')

# Loop sum for icecream scoops sold in different locations
for location in sales_data:
  for scoops in location:
    scoops_sold += scoops

# Print total scoops sold
print(f'\nThe total scoops sold in all location is {scoops_sold}',\
'\n-------- Exiting Program --------- ')
