# Artificial Intelligence
# Lab 1

# 1. Prime number

num = input('Enter any number:')
num = int(num)

count = 0

if num == 0 or num == 1:
    print(num, 'is not a Prime number')
else:
    for i in range(2, num):
        if(num % i == 0):
            count = count + 1

    if(count == 0):
        print(num, 'is a Prime number')
    else:
        print(num, 'is not a Prime number')

# 2. Simple Reflex Agent

temp = input('Enter the temperature:')
temp = float(temp)

threshold = 28.0

if temp > threshold:
    print('Since the temperature', temp, 'is above threshold value, AC is turned ON')
else:
    print('Since the temperature', temp, 'is below threshold value, AC is turned OFF')

# 3. Factorial

num = input('Enter any number:')
num = int(num)


fac = num

for i in range(1, num):
    fac*=i

print('Factorial of', num, 'is', fac)

# 4. Fibonacci

num = input('Enter the number of digits:')
num = int(num)

prev = 0
n = 1

for i in range(num):
    print(prev, end=' ')
    prev, n = n, prev + n

# 5. Calculator

while True:
    c = input("Enter your operation('E' to Exit):")

    if(c.upper() == 'E'):
        break
    else:
        n1 = input('Enter your first number:')
        n1 = int(n1)
        n2 = input('Enter your second number:')
        n2 = int(n2)

        result = 0

        if(c == '+'):
            result = n1 + n2
        elif(c == '-'):
            result = n1 - n2
        elif(c == '*' or c == 'x'):
            result = n1 * n2
        elif(c == '/'):
            result = n1 / n2
        else:
            print('Invalid Input!')

    print('Result:', result)

# 6. Random guessing Game

import random

count_right = 0
count_wrong = 0

while True:
    a = int(input('Enter your lower limit:'))
    b = int(input('Enter your upper limit:'))
    r = random.randint(a, b)

    while True:
        x = input('Enter your number:')
        x = int(x)

        if(x == 0):
            break

        if(x == r):
            count_right = count_right + 1
            break
        else:
            count_wrong = count_wrong + 1

# Hash_Tables with a mailbox of size 5
