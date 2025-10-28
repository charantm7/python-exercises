
# for loop
import math

n = 5
# 5,4,3,2,1
fact = 1
for i in range(1, n+1):
    fact *= i

print(fact)


# while loop
i = 1
fact = 1
n = 5
while i <= n:

    fact *= i
    i += 1

print(fact)


# reursion
def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

# using built-in keyword
print(math.factorial(5))
