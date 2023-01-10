list1 = [x*x for x in range(10)]
print("List1 is: {}".format(list1[:]))
list2 = [y*y for y in range(11,20)]
print("List2 is: {}".format(list2[:]))
#list1.append(list2)# append add list2 as a single element at end of list1
list3=list1+list2 # + make two list's elements into one new list
print("List3 is: {}".format(list3[:]))
list1.pop()
print("List3 is: {}".format(list3[:]))
# for i in range(10):
#     list1.pop()
#     print(list1[:])