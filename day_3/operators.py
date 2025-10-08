import math
#1 2 3
age = 20
height = 1.78
complex_number = 1 + 1j

print('age int: ', age)
print('height float: ', height)
print('complex number: ', complex_number)

#4
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = int(0.5 * base * height)
print('The area of the triangle is', area)

#5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_triangle = int(a + b + c)
print('perimeter of the triangle is', perimeter_triangle)

#6
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_rectangle = int(length * width)
perimeter_rectangle = 2 * area_rectangle
print("The area of rectangle: ", area_rectangle)
print("perimeter of the rectangle: ", perimeter_rectangle)

#7
radius = int(input("Enter radius: "))
circle_area = 3.14 * (radius**2)
circle_circumference = 2 * 3.14 * radius
print('Circle area', circle_area)
print('circle circumference', circle_circumference)

#8
# slope = 2, x-intercept = 1, y-intercept = -2

#9
x1, y1 = 2, 6
x2, y2 = 2, 10
if x2 - x1 != 0:
    m = (y2 - y1)/ (x2 - x1) 
    print("Slope:", m)
else:
    m = float('inf')
    print("Slope is undifined")
euclidean_distance =math.sqrt(((y2 - y1)**2) + ((x2 - x1)**2)) 
print("euclidean distance", euclidean_distance)

#10
print("Compares slopes off tasks 8 and 9", 2 == m)

#11
print("if x is -3 in the formula (y = x^2 + 6x + 9) then y is:", ((-3)**2) + (6*(-3)) + 9)

#12
print("python and dragon do not have the same length: ", len("python") != len("dragon"))

#13
print("Does python and dragon both have on in there string:", ("on" in "python" and "on" in "dragon"))

#14
print("Does I hope this course is not full of jargon contain jargon:","I hope this course is not full of jargon" in "jargon")

#15
print("There is no on in dragon and python:", "on" not in "dragon and python")

#16
python = str(float(len("python")))
print("The type of the string python:", type(python))

#17
print("Number is even:", int(input("Put in number to check if it is even:")) % 2 == 0)

#18
print("Does this 7//3 equal int(2.7):", 7//3==int(2.7))

#19
print("type('10') == type(10):", type('10') == type(10))

#20
print("type('9.8') == type(10):", type('9.8') == type(10))

#21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)

#22
years = int(input("Enter number of years you have lived: "))
amount_of_seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for", amount_of_seconds_lived)

#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")