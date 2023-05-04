line = input("Enter line: ")
if len(line) >=2:
    print(f"{line[:2]}{line[-2:]}")
else:
    print("")