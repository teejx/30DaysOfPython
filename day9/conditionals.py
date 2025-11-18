# -------------------
# Exercises: Level 1
# -------------------

# 1.  Get user input using input("Enter your age: "). If user is 18 or older, give feedback: You are old enough to drive. 
#     If below 18 give feedback to wait for the missing amount of years.
# age = input('Enter your age: ')
# amount_of_years = 18 - int(age) 
# if int(age) > 18:
#     print('You are old enough to drive.')
# else:
#     print('You need' ,amount_of_years, 'more years to learn to drive.')

# 2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
#     to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for
#     bigger differences, and a custom text if my_age
# my_age = 22
# your_age = int(input('Enter your age: '))
# if int(my_age) == int(your_age)+1:
#     print('You are', int(your_age) - int(my_age), 'year older than me')
# elif int(my_age) == int(my_age)-1:
#     print('You are', int(my_age) - int(your_age), 'year younger than me')
# elif int(your_age) > my_age:
#     print('You are', int(your_age) - int(my_age), 'years older than me')
# elif int(your_age) < my_age:
#     print('You are', int(my_age) - int(your_age), 'years younger than me')
# else:
#     print('We are the same age')
    
# 3.  Get two numbers from the user using input(). Compare them and print whether a is greater, smaller, or equal to b.
# first = input('Enter your first number: ')
# second = input('Enter your second number: ')
# a = int(first)
# b = int(second)

# if a > b:
#     print('Your FIRST number is greater than your SECOND number')
# else:
#     print('Your SECOND number is greater than your FIRST number')


# -------------------
# Exercises: Level 2
# -------------------


# 4.  Write a code which gives grade to students based on their scores:
#     90-100 = A, 70-89 = B, 60-69 = C, 50-59 = D, 0-49 = F
# student_grade = input('Enter your grade: ')
# grade = int(student_grade)
# if 90 <= grade <= 100:
#     print('Your final grade is A')
# elif 70 <= grade <= 89:
#     print('Your final grade is B')
# elif 60 <= grade <= 69:
#     print('Your final grade is C')
# elif 50 <= grade <= 59:
#     print('Your final grade is D')
# else:
#     print('Your final grade is F')

# 5.  Check if the input month belongs to Autumn, Winter, Spring, or Summer.
# spring = 'March','April','May'
# summer = 'June','July','August'
# autumn = 'September','October','November'
# winter = 'December','January','February'

# user = input('Enter a month: ').title()

# if user in spring:
#     print('That month\'s season is spring')
# elif user in summer:
#     print('That month\'s season is summer')
# elif user in autumn:
#     print('That month\'s season is autumn')
# elif user in winter:
#     print('That month\'s season is autumn')
# else:
#     print('Invalid month')

# 6.  Using the fruits list, chek if a fruit exists. If not, add it. If it exists, print a message.
#     fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits = ['banana', 'orange', 'mango', 'lemon']
# user = input('Enter a name of a fruit: ')

# if user in fruits:
#     print('That fruit already exist in the list.')
# else:
#     fruits.append(user)
#     print(fruits)


# -------------------
# Exercises: Level 3
# -------------------


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# 7.  Check if the person dictionary has a skills key. If so, print the middle skill.
if person['skills']:
    print(person['skills'][2])
else:
    print('It does not exist.')
# 8.  Check if the person has the 'Python' skill and print the result.
if 'Python' in person['skills']:
    print('Python is found in skills')
else:
    print('It does not exist.')

# 9.  Determine if the person is a front-end, back-end, or full-stack developer based on their skills.
skills = person['skills']

front_end = {'JavaScript','React'}
back_end = {'Node','MongoDB'}

is_front = front_end.issubset(skills)
is_back = back_end.issubset(skills)

if is_front and is_back:
    print('The person is a Full-Stack developer.')
elif is_front:
    print('The person is a Front-End developer.')
elif is_back:
    print('The person is a Back-End developer.')
else:
    print('The person\'s developer type cannot be determined.')

# 10.  If the person is married and lives in Finland, print:
#      "<first_name> <last_name> lives in Finland. He is married."
first_name = person['first_name']
last_name = person['last_name']
country = person['country']
marry = person['is_married']

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in Finland. He is married.')
