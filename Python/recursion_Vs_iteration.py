'''number = int(input('give a number'))
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))
print(factorial(number))'''
'''
number = [int(a) for a in input().split()]
def recursion(number):
    if len(number) == 2:
        return number[0] + number[1]
    elif len(number) == 1:
        return number[0]
    else:
        mid = len(number) // 2
        return recursion(number[mid:]) + recursion(number[:mid])
print(recursion(number))'''

number = int(input('Give a number'))
fibonacci = [0, 1]
def sequance(n):
    if len(fibonacci) == n:
        print(fibonacci)
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        sequance(n)
sequance(number)