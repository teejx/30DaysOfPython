# ============================
#    EXERCISES — LEVEL 1
# ============================

# 1. Declare an empty list
empty_list = list()

# 2. Declare a list with more than 5 items
random = ['dog','computer','human','cat','food']
print(type(random))

# 3. Find the length of your list
print('random has',len(random),'length')

# 4. Get the first item, the middle item, and the last item of the list
first = random[0]
print(first)
middle = random[2]
print(middle)
last = random[4]
print(last)

# 5. Declare a list called mixed_data_types with: name, age, height, marital status, address
mixed_data_types = ['Tehrence', 22, '173cm', True, {'address':'Taguig City, Philippines'}]
print(mixed_data_types)

# 6. Declare a list named it_companies with: Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# 7. Print the it_companies list
print(it_companies)

# 8. Print the number of companies in the list
print('the list has',len(it_companies),'companies')

# 9. Print the first, middle, and last company
first_company = (it_companies[0])
print(first_company)
middle_company = (it_companies[3])
print(middle_company)
last_company = (it_companies[6])
print(last_company)

# 10. Modify one of the companies and print the list
modified = len(it_companies) -3
it_companies[modified] = 'Accenture'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('IBM')
print(it_companies)

# 12. Insert an IT company in the middle of the list
it_companies.insert(4, 'Alphabet')
print(it_companies)

# 13. Change one IT company name to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

# 14. Join the it_companies list with a string '#;  '
join = '#;  '.join(it_companies)
print(join)

# 15. Check if a certain company exists in it_companies
exists = 'Apple' in it_companies
print(exists)

# 16. Sort the list using sort()
it_companies.sort()
print(it_companies)

# 17. Reverse the list using reverse()
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies
print(it_companies[3:])

# 19. Slice out the last 3 companies
print(it_companies[:-3])

# 20. Slice out the middle company or companies
middle_one = len(it_companies) // 2
print(it_companies[:middle_one] + it_companies[middle_one+1:])

# 21. Remove the first IT company from the list
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
companies.pop(0)
print(companies)

# 22. Remove the middle IT company or companies
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
companies.pop(3)
print(companies)

# 23. Remove the last IT company from the list
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
companies.pop(6)
print(companies)

# 24. Remove all IT companies from the list
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
companies.clear()
print(companies)

# 25. Destroy the it_companies list completely
companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del companies

# 26. Join front_end and back_end lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
combined = front_end + back_end
print(combined)

# 27. Copy the joined list into full_stack, then insert Python and SQL after Redux
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(['Python', 'SQL'])
full_stack = front_end + back_end
print(full_stack)

# ============================
#    EXERCISES — LEVEL 2
# ============================

# 28. Given ages list:
#       ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#     Sort it and find the min and max age=[]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
print(min_age)
max_age = max(ages)
print(max_age)

# 29. Add the min and max age again to the list
ages.extend((19,26))
print(ages)

# 30. Find the median age
median = len(ages)
a = median / 2
b = (median + 1) / 2
print(a)
print(b)
results = (ages[5] + ages[6]) // 2
print(results)

# 31. Find the average age (sum / count)
average = sum(ages) / len(ages)
print('Average Age is', average)

# 32. Find the age range (max - min)
range = max_age - min_age
print(range)

# 33. Compare |min - average| and |max - average| using abs()
min_compare = (min_age - average)
max_compare = (max_age - average)
compare = max_compare > min_compare
print(compare)

# 34. Find the middle country/countries from:
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', ]
countries_count = len(countries) // 2 - 1
countries_count1 = len(countries) // 2
middle_country = countries[countries_count], countries[countries_count1]
print(middle_country)

# 35. Divide the countries list into two equal halves (if odd, first half gets one extra element)
mid = (len(countries) + 1) // 2
print(mid)
print('first half:',countries[:mid])
print('second half:',countries[mid:])

# 36. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn,rs,us, *scandic = countries1
print(cn)
print(rs)
print(us)
print(scandic)