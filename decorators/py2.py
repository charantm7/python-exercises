# Log before and after

def logs(function):
    def logger(*args):
        print("Function Starting")
        function(*args)
        print("Function ending")
    return logger


@logs
def count():
    var = 'hello i am charan'
    print(len(var))


@logs
def multipels(num):

    for i in range(1, 11):
        print(f"{num}*{i}={num*i}")

    print('\n')


# multipels(5)

# upper case conversion
def CaseValidation(function):
    def upperConversion():
        func = function()
        cased = func.upper()
        return cased
    return upperConversion


@CaseValidation
def cars():
    return "This is my cars"


print(cars())
