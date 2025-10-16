#level1
#1
empty_list = list()

#2
list_more_5 = [0, 1, 2, 3, 4, 5]

#3
print(len(list_more_5))

#4
print(list_more_5[0])
print(list_more_5[len(list_more_5)//2])
print(list_more_5[-1])

#5
mixed_data_types = ["Jannis", 20, 1.78, "Single", "address"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print("Number of companies:", len(it_companies))

#9
print(it_companies[0])
print(it_companies[len(list_more_5)//2])
print(it_companies[-1])

#10
it_companies[0] = "Google"
it_companies[1] = "Facebook"
print(it_companies)

#11
it_companies.append("Tesla")
print(it_companies)

#12
it_companies.insert(len(list_more_5)//2, "inserted company in the midle")
print(it_companies)

#13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
print('#; '.join(it_companies))

#15
print("Check if Facebook is in the list it_companies:", "Facebook" in it_companies)

#16
it_companies.sort()
print("Sorted list:", it_companies)

#17
it_companies.reverse()
print("Reversed list:", it_companies)

#18
first_three = it_companies[:3]
print("First 3 companies:", first_three)

#19
last_three = it_companies[-3:]
print("Last 3 companies:", last_three)

#20
print(it_companies[len(it_companies)//2])

#21
it_companies.pop(0)
print(it_companies)

#22
it_companies.pop(len(it_companies)//2)
print(it_companies)

#23
it_companies.pop(-1)
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_var = ages[0]
max_var = ages[-1]
print("min:", min_var)
print("max:", max_var)
min_max_sum = min_var + max_var
ages.append(min_max_sum)
print(ages)

#median
n = len(ages)
if n % 2 != 0:
    # Odd number of elements: middle element
    median_age = ages[n // 2]
else:
    # Even number of elements: average of two middle elements
    middle1 = ages[n // 2 - 1]
    middle2 = ages[n // 2]
    median_age = (middle1 + middle2) / 2

print("Median age:", median_age)

average_age = sum(ages) / len(ages)
print("average age:", average_age)

age_range = max(ages) - min(ages)
print("age range:", age_range)

min_average = abs(min(ages) - average_age)
max_average = abs(max(ages) - average_age)

print("min average:", min_average)
print("max average:", max_average)
#2
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

n = len(countries)
if n % 2 != 0:
    # Odd number of elements: middle element
    print(countries[n // 2])
else:
    # Even number of elements: Two middle elements
    middle1 = countries[n // 2 - 1]
    middle2 = countries[n // 2]
    print(middle1, middle2)
#3
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries2

print("First country:", first)
print("Second country:", second)
print("Third country:", third)
print("Scandic countries:", scandic_countries)