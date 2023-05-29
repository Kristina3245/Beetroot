def outer_function():
    def inner_function():
        print("Inside inner function")

    return inner_function

my_func = outer_function()
my_func()