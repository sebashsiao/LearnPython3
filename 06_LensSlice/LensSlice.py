# Project 006: LEN'S SLICE

# Topping list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Prices list
prices = [2, 6, 1, 3, 2, 7, 2]

# Count ocurrences of $2 slices
num_two_dollar_slices = prices.count(2)
print(f'$2 slices #: {num_two_dollar_slices}\n')

# Find length of toppings list
num_pizzas = len(toppings)

# Print
print('We sell ' + str(num_pizzas) + ' diffenrent kind of pizza!\n')

# Create 2d list
pizza_and_prices = [[price, topping] for topping, price in zip(toppings, prices)]

print(pizza_and_prices,'\n')

# Cheapest pizza
cheapest_pizza = sorted(pizza_and_prices)[0]

print(f'The cheapest pizza is {cheapest_pizza}\n')

# Priciest pizza
priciest_pizza = sorted(pizza_and_prices)[-1]

print(f'The priciest pizza is {priciest_pizza}\n')

# Remove pizza
pizza_and_prices.remove(priciest_pizza)
# Add new pizza
pizza_and_prices.append([2.5, 'Peppers'])

# sort pizza by price (ascending)
pizza_and_prices.sort()

print(f'Updated list of available pizzas: \n{pizza_and_prices}\n')

# 3 cheapest pizzas
three_cheapest = sorted(pizza_and_prices)[:3]

print(f'The three cheapest pizzas are: {three_cheapest}')

