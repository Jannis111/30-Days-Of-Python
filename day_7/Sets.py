#level 1
#1
#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies.update({"Tesla", "Netflix", "Adobe"})
print(it_companies)

#4
it_companies.remove("Adobe")
print(it_companies)

#5
#remover() raises a KeyError when the element is not found and discard() does not.

#level 2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_B = A.union(B)
print(A_B)

#2
A_B_intersect = A.intersection(B)
print("Intersect between A and B:", A_B_intersect)

#3
print("Is A subset of B:", A.issubset(B))

#4
print("Are A and B disjoint sets:", A.isdisjoint(B))

#5
join_A_B = A.union(B)
join_B_A = B.union(A)
print(join_A_B)
print(join_B_A)

#6
symmetric_difference_A_B = A.symmetric_difference(B)
print("symmetric difference between A and B:", symmetric_difference_A_B)

#7
del A 
del B

#level 3
#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_list_len = len(age)
age = set(age)
age_set_len = len(age)

print("age list length:", age_list_len)
print("age set length:", age_set_len)

#2
#string: a sequence of charcters enclosed in quotes "" or ''
#list: a collection of element enclosed in square brackets [ ]
#tuple: A collection of immutable elements enclosed in parentheses ( )
#set: An unordered collection of unique elements enclosed in { }

#3
word = "I am a teacher and I love to inspire and teach people."
unique_words = set(word.split(" "))
print("unique words", len(unique_words))