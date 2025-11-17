# -------------------
# Exercises: Level 1
# -------------------

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.  Find the length of the set it_companies
print(len(it_companies))

# 2.  Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3.  Insert multiple IT companies at once to the set it_companies
it_companies.update(['Alphabet','Accenture'])
print(it_companies)

# 4.  Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# 5.  What is the difference between remove and discard
# remove() method raises an error when an error is made so it's better to use for checking while discard() does not raise any error so it's not okay to use for checking

# -------------------
# Exercises: Level 2
# -------------------

# 6.  Join A and B
C = A.union(B)
print(C)

# 7.  Find A intersection B
print(A.intersection(B))

# 8.  Is A subset of B
subset = A.issubset(B)
print(subset)

# 9.  Are A and B disjoint sets
disjoint = A.isdisjoint(B)
print(disjoint)

# 10.  Join A with B and B with A
AwithB = A.union(B)
BwithA = B.union(A)
print(AwithB)
print(BwithA)

# 11.  What is the symmetric difference between A and B
difference = A - B
print(difference.union(B - A))

# 12.  Delete the sets completely
del it_companies, A, B

# -------------------
# Exercises: Level 3
# -------------------

# 13.  Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age))
print(len(age_set))

# 14.  Explain the difference between the following data types: string, list, tuple and set
# String is a datatype where you can store things such as letters, numbers and special characters
# List is a collection of ordered and changeable items
# Tuple is a collection of ordered and unmutable or unmodifiable items
# Set is a a collection of unordered and changeable items, removes duplicates items

# 15.  I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = ('I am a teacher and I love to inspire and teach people.')
splitted = sentence.split()
fixed = set(splitted)
print(fixed)
print(len(fixed))
