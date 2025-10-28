

def custom_range_function(start, stop=None, step=1):

    if stop is None:

        stop = start
        start = 0

    current = start

    if step > 0:

        while current < stop:
            yield current
            current += step

    else:
        while current > stop:
            yield current
            current += step


def my_gen():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("Done")


if __name__ == "__main__":
    print("This is the loops and ranges")

    print(list(custom_range_function(1, 11, 1)))
    # this command will all when the file is run directly and not the imported one
