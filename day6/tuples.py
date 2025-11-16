# -------------------
# Exercises: Level 1
# -------------------

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Torti','Stella','Tiny','Silvi')
brothers = ('Sunny', 'Moeby', 'Bossy')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ('Dad', 'Mom')
modified = siblings + family_members
print(modified)

# -------------------
# Exercises: Level 2
# -------------------

# 1. Unpack siblings and parents from family_members
first, second, third, fourth, fifth, sixth, seventh, *parents = modified
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple','Orange','Grapes')
vegetables = ('Broccoli','Carrot','Lettuce')
animal_products = ('Shampoo','Leash','Collar')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = (len(food_stuff_tp)) // 2
print(food_stuff_tp[:middle]+ food_stuff_tp[middle+1:])
# OUTPUT: 'Apple', 'Orange', 'Grapes', 'Broccoli', 'Lettuce', 'Shampoo', 'Leash', 'Collar'  - sliced out 'Carrot'

# 5. Slice out the first three items and the last three items from food_staff_lt list
minus_three = (len(food_stuff_lt)) -3
print(food_stuff_lt[3:minus_three])
print(food_stuff_lt[3:-3])

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#    - Check if 'Estonia' is a nordic country
#    - Check if 'Iceland' is a nordic country
#    - nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Iceland' in nordic_countries)
print('Estonia' in nordic_countries)
checkindex = nordic_countries.index('Iceland')
print(checkindex)
checkindex = nordic_countries.index('Estonia')
print(checkindex)
