#level 1 
#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [x for x in numbers if x <= 0]
print(negatives_and_zero)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print(flattened)

#3
list_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_tuples)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
c_flattened = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(c_flattened)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_new = [{f"country: {country.upper()}", f"city: {capital.upper()}"} for sublist in countries for country, capital in sublist]
print(countries_new)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(full_names)

#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1, 2, 3, 6))