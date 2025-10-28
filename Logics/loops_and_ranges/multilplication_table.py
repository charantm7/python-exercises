def multiplication(n):

    i = 1
    while i <= 10:

        print(f"{n} * {i} = {n*i}")
        i += 1


n = 5
print([f"{n} * {i} = {n*i}" for i in range(1, 11)])


# if __name__ == "__main__":

#     multiplication(5)
