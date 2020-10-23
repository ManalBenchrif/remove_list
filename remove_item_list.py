#In Python, list's methods clear(), pop(), and remove() are used to remove items (elements) from a list. 
#It is also possible to delete items using del statement by specifying a position or range with an index or slice.
 
# clear():Remove all items
#The index at the beginning is 0
liste_item=[1,5,70,-1,100]
print(liste_item)
liste_item.clear()
print(liste_item)

#pop(): Remove an item by index and get its value
list2=[5,2,-7,88,0,4,16]
print(list2)
print(list2.pop(2)) #delete -7
print(list2)

#You can use negative values to specify the position from the end. The index at the end is -1.
print(list2.pop(-2)) #delete 4
print(list2)

#If the argument is omitted, the last item is deleted.
print(list2.pop())
print(list2)

#Specifying a nonexistent index raises an error.
#print(list2.pop(50)) #IndexError: pop index out of range

#remove() : Remove an item by value:
#If the list contains more than one matching the specified value, only the first one is deleted.
list3=[1,5,-80,74,-9,56,3]
print(list3)
list3.remove(-80)
print(list3)

#del statements.: Remove items by index or slice:
#Specify the item to be deleted by index. The first index is 0, and the last index is -1.
del list3[2] # delete list3[2]=74
print(list3)

#Using slice, you can delete multiple items at once.
list4=[9,4,5,-12,0,3,7,47,15,-8]
print(list4)
del list4[3:6] #delete -12,0,3
print(list4)
del list4[4:]  #delete 47,15,-8
print(list4)
del list4[-2:] #delete 5,7
print(list4)

#It is also possible to delete all items by specifying the entire range.
del list4[:]
print(list4)

#Remove multiple items that meet the condition: List comprehensions
#Removing items that satisfy the condition is equivalent extracting items that do not satisfy the condition.
#For this purpose, list comprehensions are used.
l = ['manal', 'salma', 'basma', 'manal','nihal']
print(l)
print([s for s in l if s != 'manal']) #['salma', 'basma', 'nihal']
print(l)
print([s for s in l if s.endswith('a')]) #['salma', 'basma']
print(l)











