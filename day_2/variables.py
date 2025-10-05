import math

# Day 2: 30 Days of python programming
# Exercise 1 & 2
first_name = input("first name: ")
last_name = input("last name: ")
full_name = "Jannis Geerts"
country = input("Country: ")
city = "Wageningen"
age = input("age: ")
year = 2025
is_married = False
is_true = True
is_light_on = False
multiple_var1, multiple_var2, multiple_var3 = 1, 2, 3

#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(multiple_var1))
print(type(multiple_var2))
print(type(multiple_var3))

print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one//num_two
#area of circle A:area r:radius; A = π*r^2
# circumference of a circle C:circumference d:diameter r:radius; C = π*d or C = 2πr
area_of_circle = math.pi * (30 ** 2)
circum_of_circle = math.pi * 30 * 2
user_area_of_circle = math.pi * (int(input("Enter radius: ")) ** 2)

print(total)
print(diff)
print(remainder)
print(exp)
print(floor_division)

print(area_of_circle)
print(circum_of_circle)
print(user_area_of_circle)