adhoc=[1,2,3,1,4,5,66,22,6,0,9]
list1=[]
list2=[]
for i in adhoc:
	if i>5:
		list1.append(i)
print(list1)
for i in adhoc:
	if i<=2:
		list2.append(i)
print(list2)
print("number is greater than 5 list is here------>>>")
print(list1)
print("number is less than or equal to 2 list is here --------->>>>>")
print(list2)