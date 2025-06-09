list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#USING LIST SLICING AND LOOP

print('Original list: ',list1)
print('Extracted first five elements: ',list1[0:5])
list2=[]
for i in range(5):
    list2.append(list1[i])
list2.reverse()
print('Reversed extracted elements: ',list2)

#USING LOOP WITH APPEND
'''
list2=[]
for i in range(5):
    list2.append(list1[i])
print('Original list: ',list1)
print('Extracted first five elements: ',list2)
list2.reverse()
print('Reversed extracted elements: ',list2)
'''