#level 1
#1
dog = {}

#2
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 5

print(dog)

#3
student = {}
student["first_name"] = "Alice"
student["last_name"] = "Johnson"
student["gender"] = "Female"
student["age"] = 22
student["marital_status"] = "Single"
student["skills"] = ["Python", "Data Analysis", "Machine Learning"]
student["country"] = "USA"
student["city"] = "New York"
student["address"] = "123 Maple Street"
print(student)

#4
print("Student dictonary length:", len(student))

#5
print("Student value type of skills:", type(student.get("skills")))

#6
student["skills"].extend(["Deep Learning", "Data Visualization"])
print("Skills with two new added skills:", student["skills"])

#7
student_key_list = list(student.keys())
print(student_key_list)

#8
student_value_list = list(student.values())
print(student_value_list)

#9
student_tuples = list(student.items())
print(student_tuples)

#10
student.pop("address")
print(student)

#11
del student