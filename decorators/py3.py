from ast import arg
import time

# Decorators


def timeTracker(function):

    def tracker():
        start = time.perf_counter()
        function()
        end = time.perf_counter()
        print(f"Execution Time: {end-start:0.9f} seconds")

    return tracker


def runNTimes(n):
    def deco(function):
        def runner(*args):
            for _ in range(n):
                function(*args)

        return runner
    return deco


@runNTimes(10)
def infoTech(message):
    print(message)


# only allow even numbers

def filterEvenOnly(function):

    def even(*args):
        for arg in args[0]:
            print(arg)
            if arg % 2 == 0:
                function(arg)
            else:
                print('number is not even')

    return even


@filterEvenOnly
def home(num):
    print(f'this is the num {num}')


# home([5, 6, 7, 2])

# a = [5, 6, 3, 6, 3]

# for i in a:
#     print(type(i))

def cache(function):
    value = {}

    def store(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))

        if key in value:
            print('cached')
            return value[key]

        else:

            func = function(*args, **kwargs)

            value[key] = func
            return func

    return store


@cache
def hi(message):
    return message


print(hi('hi'))
print(hi('hi'))
print(hi('hello'))
print(hi('hello'))
