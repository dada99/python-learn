import os
file = 'vm-list.txt'
vmList = []
with open(file,'r') as f:
    for x in f: # Read each line of the file
        #print(os.system('ping %s'%x))
        vmList.append(x.strip())
    # vmList = [x.strip() for x in f]    
vmList.sort()

for x in vmList:
    print(x)


# for i in vmList:
#     print(os.system('ping %s'%i))