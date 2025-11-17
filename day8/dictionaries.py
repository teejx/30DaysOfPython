# -------------------
# Exercises: Level 1
# -------------------

# 1.  Create an empty dictionary called dog
dog = {}
print(type(dog))

# 2.  Add name, color, breed, legs, age to the dog dictionary
dog['name','color','breed','legs','age'] = 'Moeby', 'Brown', 'Shihtzu', 'short', '3'

# 3.  Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Tehrence',
    'last_name':'Llenarez',
    'gender':'Male',
    'age': 22,
    'marital status':'Single',
    'skills':['Python'],
    'country':'Philippines',
    'city':'Taguig',
    'address':'Example'
}

# 4.  Get the length of the student dictionary
print(len(student))

# 5.  Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# 6.  Modify the skills values by adding one or two skills
student['skills'].extend(['Gaming','Problem Solving'])
print(student['skills'])

# 7.  Get the dictionary keys as a list
print(student.keys())

# 8.  Get the dictionary values as a list
print(student.values())

# 9.  Change the dictionary to a list of tuples using items() method
change = tuple(student.items())
print(type(change))

# 10.  Delete one of the items in the dictionary
del student['address']

# 11.  Delete one of the dictionaries
del dog
