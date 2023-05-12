def oops():
    raise IndexError("An IndexError occurred")
def catch_error():
    try:
        oops()
    except IndexError as a:
        print(a)
catch_error()

#If I change IndexError to KeyError expection will not be catched
