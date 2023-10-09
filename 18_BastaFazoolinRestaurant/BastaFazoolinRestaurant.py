# Building Buz
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return 'Business name: {name} \nFranchises: {franchises}'.format(name=self.name, franchises=self.franchises)


# Creating Franchises
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return 'Location: {address}'.format(address=self.address)

    def available_menus(self, time):
        return [menu for menu in self.menus if time >= menu.start_time and time <= menu.end_time]


# Making Menus
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{name} menu available from {start_time} to {end_time}'.format(name=self.name,
                                                                              start_time=self.start_time,
                                                                              end_time=self.end_time)

    # for items passing as list in purchased_items parameter
    def calculate_bill(self, purchased_items):
      total_bill = 0
      for item in purchased_items:
        total_bill += self.items.get(item, 0)
      return total_bill

    # # altern way for items passing as *args in purchased_items parameter
    # def calculate_bill(self, *purchased_items):
    #     purchased_items = [self.items.get(items, 0) for items in purchased_items]
    #     return sum(purchased_items)


# Menus Buz_01 - "Basta Fazoolin' with my Heart"
# brunch menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('brunch', brunch_items, '11am', '4pm')

# early_bird menu
early_birld_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                     'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                     'coffee': 1.50, 'espresso': 3.00, }
early_bird_menu = Menu(name='early_bird', items=early_birld_items, start_time='3pm', end_time='6pm')

# dinner menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }
dinner_menu = Menu(name='dinner', items=dinner_items, start_time='5pm', end_time='11pm')

# kids menu
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu(name='kids', items=kids_items, start_time='11am', end_time='9pm')


# Menus Buz_02 - "Take a' Arepa"
# arepas menu
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu(
    name='arepas',
    items=arepas_items,
    start_time='10am',
    end_time='8pm'
)


print('_____ . TESTING LINE BASTA . _____')

print(brunch_menu, early_bird_menu, dinner_menu, kids_menu, sep='\n')

brunch_order_1 = brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(brunch_order_1)   # should calculate 13.5

early_bird_order_1 = early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(early_bird_order_1)   # should calculate 21.5

# print(brunch.calculate_bill('pancakes', 'home fries', 'coffee'))    # purchased_items as a *args

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

print(flagship_store, new_installment, sep='\n')
print(flagship_store.available_menus('12pm'))
print(flagship_store.available_menus('5pm'))

basta_buz = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(basta_buz)

print('-----------------------------------', sep='\n')


print('_____ . TESTING LINE AREPAS . _____')

arepas_buz = Business("Take a' Arepa", [arepas_menu])
print(arepas_buz)


arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
print(arepas_place)

print(arepas_buz.franchises[0])
