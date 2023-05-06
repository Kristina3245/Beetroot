import random
list1=[]
list2=[]
list3=[]
a=0
while a<10:
    a+=1
    list1.append(random.randint(0, 10))
    list2.append(random.randint(0,10))
print(list1)
print(list2)
for common_number in list1:
    if common_number in list2 and common_number not in list3:
        list3.append(common_number)
print(list3)