# Project: Carly's Clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


print('Std Prices: ' + str(prices))

# Prices and Cuts
total_price = 0
# sum prices
for price in prices:
  total_price += price
# altern: total_price = sum(prices)

# avegare price
average_price = total_price / len(prices)
print(f'Average Haircut Price: {average_price}')

# reduce prices by 5 dolars with list comprehension
new_prices = [p - 5 for p in prices]
print('New Prices: '+ str(new_prices))

# Revenue
total_revenue = 0
# calculate revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f'Total Revenue: {total_revenue}')

# average daily revenue
average_daily_revenue = total_revenue / 7
print('Average Daily revenue: ' + str(average_daily_revenue))

# advertising haircut under $30 with list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)

# same but using for loop
cuts_under_30 = []
for i in range(len(hairstyles)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30)

