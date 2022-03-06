#level-1
#1
print(tuple())
#2
cities_west = ('London','New York','Barcelona','Madrid','Amsterdam')
cities_east = ('Tokiyo','Beijing','New Delhi','Dubai','Riyadh')
cities_world = cities_west + cities_east #3
print(cities_world)
print(len(cities_world)) #4
print('Lahore' in cities_world)
#5
cities_world_1 = list(cities_world)
print(cities_world_1)
cities_world_1.append('Mumbai')
print(cities_world_1)
cities_world = tuple(cities_world_1)
print(cities_world) 
#level-2
#1
first_city, second_city, third_city, *rest = cities_world
print(first_city)
print(second_city)
print(third_city)
print(rest)
#2
fruits = ('Mango','Apple','Banana','Pineapple','Papapya')
vegetables = ('Potato','Tomato','Onion','Brinjal','Lemon')
animal_products = ('Butter','Milk','Ghee','Curd')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_list = list(food_stuff_tp) #3
print(food_stuff_list)
print(food_stuff_list[7:8]) #4
print(food_stuff_list[0:3]) #5
print(food_stuff_list[-3:15]) #5
food_stuff_tp = tuple(food_stuff_list)
print(food_stuff_tp)
#del food_stuff_tp #6
#print('Potato' in food_stuff_tp) #7

nordic_countries = ('Denmark','Finland','Iceland','Norway','Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
