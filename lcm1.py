# LCM
def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

# GCD
def gcd(i, j):
    if j == 0:
        return i
    else:
        return gcd(j, i % j)

# Check if two numbers are coprime
def are_coprime(a, b):
    hcf = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf == 1

# Reading two numbers
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if are_coprime(first, second):
    print('%d and %d are CO-PRIME' % (first, second))
else:
    print('%d and %d are NOT CO-PRIME' % (first, second))
