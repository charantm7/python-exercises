# first version to print even numbers
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# optimised verion of it
for i in range(2, 51, 2):
    print(i)


# better version of it
print(*range(2, 51, 2))
