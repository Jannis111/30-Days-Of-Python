#1
space = ' '
course = 'Thirty' + space + 'Days' + space + 'Of' + space + 'Python'

print(course)

#2, 3 & 4
company = 'Coding' + space + 'For' + space + 'All'
print(company)

#5
print("Company string length:", len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize()) 
print(company.title())       
print(company.swapcase())    

#9
print(company[:6])

#10
print(company.find("Coding"))

#11
print(company.replace("Coding", "Python"))

#12
slogan = "Python for Everyone"
print(slogan.replace("Everyone", "All"))

#13
print(company.split(" "))

#14
big_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_companies.split(" "))

#15
print(company[0])

#16
print(company[-1])

#17
#space
print(company[10])

#18
slogan_split = slogan.split(" ")
slogan_acronym = "".join(slogan[0] for slogan in slogan_split)
print(slogan_acronym)

#19
words = company.split(" ")
acronym = "".join(word[0] for word in words)
print(acronym)

#20
print(company.index("C"))

#21
print(company.index("F"))

#22
print(company.rfind("i"))

#23
print("You cannot end a sentence with because because because is a conjunction".index("because"))

#24
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

#25
print("You cannot end a sentence with because because because is a conjunction".replace(" because because because ", ""))

#26
print("You cannot end a sentence with because because because is a conjunction".index("because"))

#27
print("You cannot end a sentence with because because because is a conjunction".replace(" because because because ", ""))

#28
print("Coding For All".startswith("Coding"))

#29
print("Coding For All".endswith("coding"))

#30
print(" Coding For All ".strip())

#31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32
libraries = "# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']) 
print(libraries)

#33
print("I am enjoying this challenge.\nI just wonder what is next.")

#34
print("Name\tAge\tCountryCity\tAsabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
