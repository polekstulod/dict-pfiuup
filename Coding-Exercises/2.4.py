flavor = ['vanilla', 'chocolate', 'strawberry', "cookies n' cream", 'bubblegum']
toppings = ['almonds', 'banana slices', 'chocolate syrup', 'caramel syrup', 'while chocolate chips']

ice_cream = dict(zip(flavor, toppings))

print(ice_cream)

ice_cream['chocolate'] = 'blueberries'
ice_cream.update({'matcha': 'pistachios', 'ube': 'mango slices'})

print(ice_cream)
