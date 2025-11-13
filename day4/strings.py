# Exercise 4

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to 'Thirty Days Of Python'
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
print(first, second, third, fourth)

# 2. Concatenate the string 'Coding', 'For', 'All' to 'Coding For All'
one = 'Coding'
two = 'For'
three = 'All'
print(one, two, three)
# 3. Declare a variable named company and assign it the value "Coding For All"
company = 'Coding For All'

# 4. Print the variable company using print()
print(company)

# 5. Print the length of the company string using len() and print()
print(len(company))

# 6. Change all characters of company to uppercase using upper()
print(company.upper())

# 7. Change all characters of company to lowercase using lower()
print(company.lower())

# 8. Format the string "Coding For All" using capitalize(), title(), and swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice out the first word of "Coding For All"
completeword = 'Coding For All'
sliced = completeword[6:14] #
print(sliced)

# 10. Check if "Coding For All" contains the word 'Coding' using index(), find(), or other methods
print(company.index('Coding'))
print(company.find('Coding'))

# 11. Replace the word 'Coding' in "Coding For All" with 'Python'
challenge = 'Coding For All'
print(challenge.replace('Coding', 'Python'))

# 12. Change "Python for Everyone" to "Python for All" using replace() or other methods
change = 'Python for Everyone'
print(change.replace('Python for Everyone', 'Python for All'))

# 13. Split the string "Coding For All" using space as a separator
print(change.split())

# 14. Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma
separate = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(separate.split(', '))

# 15. Find the character at index 0 in "Coding For All"
print(challenge[0])

# 16. Find the last index of "Coding For All"
print(challenge[13])

# 17. Find the character at index 10 in "Coding For All"
print(challenge[10])

# 18. Create an acronym/abbreviation for "Python For Everyone"
acronym = 'Python For Everyone'
print(acronym.split()[0][0] + acronym.split()[2][0])

# 19. Create an acronym/abbreviation for "Coding For All"
abbreviation = 'Coding For All'
print(abbreviation.split()[0][0] + abbreviation.split()[1][0] + abbreviation.split()[2][0])

# 20. Use index() to determine the first occurrence of 'C' in "Coding For All"
C_occurence = 'Coding For All'
print(C_occurence.index('C'))

# 21. Use index() to determine the first occurrence of 'F' in "Coding For All"
F_occurence = 'Coding For All'
print(F_occurence.index('F'))

# 22. Use rfind() to determine the last occurrence of 'l' in "Coding For All People"
last_occurence = 'Coding For All People'
print(last_occurence.rfind('l'))

# 23. Find the first occurrence of 'because' in "You cannot end a sentence with because because because is a conjunction" using index() or find()
first_occurence = 'You cannot end a sentence with because because because is a conjunction'
print(first_occurence.index('because'))
print(first_occurence.find('because'))

# 24. Find the last occurrence of 'because' using rindex() in the same sentence
print(first_occurence.rindex('because'))

# 25. Slice out the phrase 'because because because' from the sentence
print(first_occurence[31:54])

# 26. Find the position of the first occurrence of 'because' in the sentence (duplicate of #23)
print(first_occurence.index('because'))

# 27. Slice out the phrase 'because because because' from the sentence (duplicate of #25)
print(first_occurence[31:54])

# 28. Check if "Coding For All" starts with the substring 'Coding'
check = 'Coding For All'
print(check.endswith('Coding'))

# 29. Check if "Coding For All" ends with the substring 'coding'
print(check.lower().endswith('coding'))

# 30. Remove left and right trailing spaces from '   Coding For All      '
remove = '   Coding For All      '
print(remove.strip('   '))

# 31. Check which of the following are valid identifiers: 30DaysOfPython, thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# 32. Join the list ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] with a hash and space
join = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
results = ' # '.join(join)
print(results)

# 33. Use newline escape sequence to separate these sentences:
#       "I am enjoying this challenge."
#       "I just wonder what is next."
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use tab escape sequence to write:
#       Name      Age     Country   City
#       Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use string formatting to display:
#       radius = 10
#       area = 3.14 * radius ** 2
#       "The area of a circle with radius 10 is 314 meters square."
radius = 10
area = 3.14 * radius ** 2
sentence = 'The area of a circle with radious {} is {:.0f} meters square.'.format(radius,area)
print(sentence)

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')