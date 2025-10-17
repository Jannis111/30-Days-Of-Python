import random
import string


#level 1
#1
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())

#2
def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters for each ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    
    characters = string.ascii_letters + string.digits
    ids = []
    
    for i in range(num_ids):
        user_id = ''.join(random.choice(characters) for i in range(num_chars))
        ids.append(user_id)
    
    return ids
print(user_id_gen_by_user())

#3
def rgb_color_gen():
    return f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
print(rgb_color_gen())

#level 2
#1
def list_of_hexa_colors(n):
    colors = []
    hex_chars = '0123456789abcdef'
    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(2))

#2
def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        color = f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
        colors.append(color)
    return colors
print(list_of_rgb_colors(2))

#3
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
print(generate_colors('hexa', 2))
#level 3
#1
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1,2,3]))
#2
def seven_unique_random_numbers():
    return random.sample(range(10), 7)
print(seven_unique_random_numbers())
