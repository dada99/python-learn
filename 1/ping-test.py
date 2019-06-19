import os
file = 'vm-list.txt'
f = open(file,'r')
vmList = []
for x in f:
    #print(os.system('ping %s'%x))
    vmList.append(x)
vmList.sort()

for x in vmList:
    print(x)


for i in vmList:
    print(os.system('ping %s'%i))