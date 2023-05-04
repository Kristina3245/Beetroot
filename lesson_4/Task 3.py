import random

num_list1 = random.randint(1, 5)
num_list2 = random.randint(1, 10)
operator = random.choice(["+", "-", "*"])
guess=int(input(f"What is {num_list1} {operator} {num_list2} ? "))
if operator=="+":
    result=num_list1+num_list2
    if result==guess:
        print("Correct!")
    else:
        print("Wrong!")
elif operator=="-":
    result=num_list1-num_list2
    if result==guess:
        print("Correct!")
    else:
        print("Wrong!")
elif operator=="*":
    result=num_list1*num_list2
    if result==guess:
        print("Correct!")
    else:
        print("Wrong!")