list1 = [x*x for x in range(10)]
print("List1 is: {}".format(list1[:]))
list2 = [y*y for y in range(11,20)]
print("List2 is: {}".format(list2[:]))
list1.append(list2)
print("List1 is: {}".format(list1[:]))
list1.pop()
print("List1 is: {}".format(list1[:]))
for i in range(10):
    list1.pop()
    print(list1[:])