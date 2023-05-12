list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dict = {index + 1: list[index] for index in range(0, len(list))}
print(dict)
newdict = {value: key for key, value in dict.items()}
print(newdict)
