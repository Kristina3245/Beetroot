import random
numbers=[]
a=0
while a<10:
    a+=1
    numbers.append(random.randint(0, 10))
print(numbers)
print(max(numbers))