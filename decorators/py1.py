def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument(*args, **kwargs):
    print("No arguments here.")


function_with_no_argument("hi", hello="hell0")


# # dec with args

# def with_args(function):
#     def wrapper(num1, num2):
#         print("my args: {0}, {1}".format(num1, num2))
#         function(num1, num2)
#     return wrapper


# @with_args
# def numbers(num1, num2):
#     print(f'this is {num1}, {num2}')


# numbers('hi', 'hello')
# import functools


# def decorator(function):

#     def wrapper():

#         func = function()
#         up = func.upper()
#         return up
#     return wrapper


# def spliting_dec(function):
#     @functools.wraps(function)
#     def wrapper():
#         func = function()
#         sp = func.split()
#         return sp
#     return wrapper


# @spliting_dec
# @decorator
# def words():
#     return "hello i am charan"


# print(words())

# def calc(data):
#     print(data)


# def call(num):
#     data = "hi"
#     return num(data)


# call(calc)


# def hello_function():
#     def say_hi():
#         return "hi"
#     return say_hi


# hi = hello_function()  # it gives the say_hi() but not called
# print(hi())  # this calls the say_func


# def decorator(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper


# @decorator
# def hi():
#     print("this is charan")


# hi()
