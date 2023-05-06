list1=list(range(1,100))
print(list1)
list2=[]
a=0
while a<len(list1):
    i=list1[a]
    if i % 7 == 0 and i % 5 != 0:
        list2.append(i)
    a+=1
print(list2)


#for i in list1:
    #if i % 7==0 and i % 5!=0:
        #list2.append(i)
#print(list2)

