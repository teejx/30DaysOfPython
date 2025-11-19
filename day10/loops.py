# -------------------
# Exercises: Level 1
# -------------------


# 1.  Iterate 0 to 10 using for loop, do the same using while loop.
# for i in range(11):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i = i + 1

# 2.  Iterate 10 to 0 using for loop, do the same using while loop.
# i = 10
# while i > 0:
#     print(i)
#     i = i - 1


# 3.  Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#       #
#       ##
#       ###
#       ####
#       #####
#       ######
#       #######

# for x in range(8):
#     for y in range(x):
#         print('#', end='')
#     print(' ')


# 4.  Use nested loops to create the following:
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #
#     # # # # # # # #

# for x in range(9):
#     for y in range(9):
#         print('#', end=' ')
#     print(' ')


# 5.  Print the following pattern:
#     0 x 0 = 0
#     1 x 1 = 1
#     2 x 2 = 4
#     3 x 3 = 9
#     4 x 4 = 16
#     5 x 5 = 25
#     6 x 6 = 36
#     7 x 7 = 49
#     8 x 8 = 64
#     9 x 9 = 81
#     10 x 10 = 100

# num = 0
# for num in range(11):
#     print(num,' x ', num, ' = ', + (num**2))
    
# 6.  Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for skill in skills:
#     print(skill)

# 7.  Use for loop to iterate from 0 to 100 and print only even numbers
# numbers = 0
# for numbers in range(0, 102, 2):
#     print(numbers)

# 8.  Use for loop to iterate from 0 to 100 and print only odd numbers
# numbers = 0
# for numbers in range(1, 100, 2):
#     print(numbers)


# -------------------
# Exercises: Level 2
# -------------------


# 9.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#     The sum of all numbers is 5050.
# total = 0
# for numbers in range(101):
#     total += numbers
# print(total)

# 10.  Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#      The sum of all evens is 2550. And the sum of all odds is 2500.
# total = 0
# total1 = 0
# for even in range(0,102,2):
#     total += even
# print('The sum of all evens is:', total)
# for odd in range(1,100,2):
#     total1 += odd
# print('The sum of all odds is:', total1)


# -------------------
# Exercises: Level 3
# -------------------


# 11.  Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', ]
# target = 'land'
# for word in countries:
#     if target in word.lower():
#         print(word)
# 12.  This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reverse_list = []
for i in reversed(fruit_list):
    reverse_list.append(i)
print(reverse_list)

# 13.  Go to the data folder and use the countries_data.py file.
#      What are the total number of languages in the data


# 14.  Find the ten most spoken languages from the data


# 15.  Find the 10 most populated countries in the world

