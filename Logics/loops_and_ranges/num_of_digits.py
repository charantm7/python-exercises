digits = 13344345

# string conversion
print(len(str(digits)))


if digits < 0:
    digits = -digits

count = 0
if digits == 0:
    count = 1
else:
    while digits > 0:

        digits //= 10
        count += 1

print(count)
