#level 1
#1
empty_tuple = ()

#2
sisters = ("Anna", "Sophia")
brothers = ("James", "Michael")

#3
siblings = sisters + brothers
print(siblings)

#4
print(len(siblings))

#5
family_members = siblings + ("Father",) + ("Mother",)
print(family_members)

#level 2
#1 
*unbox_siblings, father, mother = family_members
unbox_parents = (father, mother)
print(unbox_siblings)
print(unbox_parents )

#2
fruits = ("Apple", "Banana")
vegetables = ("Carrot", "Broccoli")
animal_products = ("Milk", "Eggs")

food_stuff_tp = fruits + vegetables + animal_products

print("Food stuff tuple:", food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

#4
length = len(food_stuff_lt)
middle_index = length // 2
if length % 2 == 0:
    # Even number of items: two middle elements
    middle_items = food_stuff_lt[middle_index - 1 : middle_index + 1]
else:
    # Odd number of items: one middle element
    middle_items = [food_stuff_lt[middle_index]]

print("Middle item(s):", middle_items)

#5
first_three = food_stuff_lt[:3]
print("First three items:", first_three)
last_three = food_stuff_lt[-3:]
print("Last three items:", last_three)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Is Estonia a nordic country:", "Estonia" in nordic_countries)
print("Is Iceland a nordic country:", "Iceland" in nordic_countries)
