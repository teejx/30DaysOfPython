# Exercise 3

age = 22
height = 173.0
complex = 2 - 2j

base = int(input('Enter base: '))
height = float(input('Enter height: '))
area = (base,height)
triangle = ((0.5 * base * height))
print('The area of the tringle is ', triangle)

a = int(input('side a: '))
b = int(input('side b: '))
c = int(input('side c: '))
perimeter = (a + b + c)
print('The perimeter of the triangle is: ', perimeter)

length = int(input('Enter lenght: '))
width = int(input('Enter width: '))
area = (length * width)
perimeter = 2 * (length + width)
print(area, perimeter)

radius_of_circle = int(input('Enter a radius of a circle: '))
area = 3.14 * radius_of_circle * radius_of_circle
circumference = 2 * 3.14 * radius_of_circle
print(area, circumference)

slope = 2
y_intercept = -2
x_intercept = -y_intercept/slope
print('Slope: ', slope)
print('Y Intercept: (0 ,',y_intercept,')')
print('X Intercept: (',x_intercept,', 0)')

m = (2-10)/(2-6)
print(m)
distance = (((2 - 10)**2) + ((2 - 6)**2)) ** 0.5
print(distance)

compare = m == slope
print('Are the slopes the same? ', compare)

x = -3
y = x**2 + 6*x +9
print(y)

print(len('Python') != len('Dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'i hope this course is not full of jargon')

print('on' not in 'python' and 'on' not in 'dragon')

text = len('python')
number = (float(text))
string = str(number)
print(string)

x = 8
even = x % 2 == 0
print(even)

floor_division = 7 // 3 == 2.7
print(floor_division)

print(type('10') == 10)

a = 9.8 == 10
print(a)

hours = (int(input('Enter hours: ')))
rate = (int(input('Enter rate per hour: ')))
print('Your weekly earning is', hours * rate)

years = (int(input('Enter number of years you have lived: ')))
print('You have lived for' , years * 31536000, 'seconds.')

table = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]

print(table[0])
print(table[1])
print(table[2])
print(table[3])
print(table[4])