#level 1
#1
age =int(input("Enter your age:"))
if(age >= 18):
    print("You are old enough to learn to drive.")
else:
    missing_amount_years = str(18 - age)
    print("You need " + missing_amount_years + " more years to learn to drive.")

#2
my_age = int(input("Enter your age: "))
your_age = int(input("Enter your friend's age: "))
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"You are older than your friend by {diff} year.")
    else:
        print(f"You are older than your friend by {diff} years.")
elif my_age < your_age:
    diff = your_age - my_age
    if diff == 1:
        print(f"Your friend is older than you by {diff} year.")
    else:
        print(f"Your friend is older than you by {diff} years.")
else:
    print("You and your friend are the same age!")

#3
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if(a > b):
    print(f"{a} is greater than {b}")
elif(a < b):
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")

#level 2
#1
score = int(input("Enter score: "))
grade = ""
if(80<= score <=100):
    grade = "A"
elif(70<= score <=79):
    grade = "B"
elif(60<= score <=69):
    grade = "C"
elif(50<= score <=59):
    grade = "D"
elif(0<= score <=49):
    grade = "F"        
print("Student score:", grade)    

#2
month = input("Enter the month: ").strip().capitalize() 
# Check the season
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = None

if season:
    print(f"The season is {season}.")
else:
    print("Invalid month entered.")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']

input_fruit = input("Enter a fruit: ")

if(input_fruit in fruits):
    print('That fruit already exist in the list')
else:
    fruits.append(input_fruit)
    print(fruits)    

#level 3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif skills_set == {'Node', 'Python', 'MongoDB'}:
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")