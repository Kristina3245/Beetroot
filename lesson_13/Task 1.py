def count_local_variables(func):
    local_vars = func.__code__.co_nlocals
    return local_vars

def example_function():
    v1 = 10
    v2 = "Hello"
    v3 = True
    v4 = [1, 2, 3]
    v5 = {"name": "Kristi", "age": 37}
    v6 = ("variable")
    v7 = 1.88

    return count_local_variables(example_function)

print(example_function())
