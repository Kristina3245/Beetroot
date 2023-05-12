def make_operation(operator, *arguments):
    if operator == "*":
        res = 1
        for x in arguments: # arguments = [6,7,8]
            res *= x
        return res
    if operator == "-":
        res = arguments[0]
        for x in arguments [1:]:
            res -= x
        return res
    if operator == "+":
        res = 0
        for x in arguments:
            res += x
        return res
print(make_operation("*", 3, 3, 3))
print(make_operation("-", 10, 4, 1))
print(make_operation("+", 2, 9, 1000000))



make_operation("*", 6, 7, 7)
