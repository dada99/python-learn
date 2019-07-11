#x,y,z 总和固定的情况下，x,y,z 为何值体积最大
max = [0,0,0]
tmp = 0
for x in range(1,159):
    for y in range(1,159):
      tmp = x*y*(158-x-y)
      if(max[2] < tmp):
          max[0] = x
          max[1] = y
          max[2] = tmp
      
print(max)