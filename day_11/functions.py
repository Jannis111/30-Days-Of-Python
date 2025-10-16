import math
import cmath 
from collections import Counter

#level 1
#1
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(2, 2))

#2
def area_of_circle(r):
    area = math.pi * r * r
    return area

print(area_of_circle(5))

#3
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return f"Error: {num} is not a number. Please provide only numbers."
    return total

print(add_all_nums(1, 2, 3))      
print(add_all_nums(1, 2, "hello"))

#4
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(0)) 

#5
def check_season(month):
    if month in ["September", "October", "November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return None
print(check_season("April"))

#6
def calculate_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    
    slope = (y2 - y1) / (x2 - x1)
    return slope

print(calculate_slope((1, 2), (3, 6)))  

#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    # Check if discriminant is negative for complex roots
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
    else:
        # Use cmath for complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return (root1, root2)

print(solve_quadratic_eqn(1, -3, 2))

#8
def print_list(items):
    for item in items:
        print(item)

print_list(['apple', 'banana', 'cherry', 'date'])

#9
def reverse_list(list):
    reversed_list = []
    for i in range(len(list)-1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list
print(reverse_list(['1', '2']))

#10
def capitalize_list_items(items):
    capitalized = []
    for item in items:
        capitalized.append(item.capitalize())
    return capitalized
print(capitalize_list_items(['apple', 'banana']))

#11
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([], 'orange'))

#12
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(['orange'], 'orange'))

#13
def sum_of_numbers(number):
    sum = 0
    for i in range(number + 1):
            sum = sum + i 
    return sum
print(sum_of_numbers(5))

#14
def sum_of_even(number):
    sum_of_all_even = 0
    for i in range(number + 1):
        if(i % 2 == 0):
            sum_of_all_even = sum_of_all_even + i
    return  sum_of_all_even
print(sum_of_even(5))

#15
def sum_of_odds(number):
    sum_of_all_odds = 0
    for i in range(number + 1):
        if(i % 2 == 1):
            sum_of_all_odds = sum_of_all_odds + i
    return sum_of_all_odds
print(sum_of_odds(5))

#level 2
#1
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds
print(evens_and_odds(10))

#2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

#3
def is_empty(value):
    return not bool(value)
print(is_empty([]))

#4
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    count = Counter(lst)
    max_freq = max(count.values())
    mode = [k for k, v in count.items() if v == max_freq]
    if len(mode) == len(set(lst)):
        return "No mode"
    return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))

#level 3
#1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(11))
#2
def all_unique(lst):
    return len(lst) == len(set(lst))
print(all_unique([1, 2, 3, 4, 5]))

#3
def all_same_type(lst):
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True
print(all_same_type([1, 2, 3, 4]))

#4
def is_valid_variable(name):
    if not isinstance(name, str) or not name:
        return False
    if name.isidentifier() and not name in {"False","True","None"}:
        return True
    return False
print(is_valid_variable("2var"))
