# sum through for loop
n = 10
total = 0
for i in range(n+1):
    total += i

# print(total)


# sum through while loop
n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
# print(total)


# formula derivation
# r = 1+2+3+...+(n-2)+(n-1)+n
# r = n+(n-1)+(n-2)+...+3+2+1
# 2r = (n+1) + (n+1) + (n+1) + (n+1) + ... + (n+1)
# 2r = n(n+1)
# r = n(n+1)//2

# the formula version of it
n = 10
total = n*(n+1)//2
# print(total)

# using sum keyword

n = 10
print(sum(range(1, n+1)))
