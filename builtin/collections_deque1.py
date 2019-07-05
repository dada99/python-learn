from collections import deque
d = deque(range(10))
print(d)
for i in d:
    print(i)
d.rotate(2) # shift 2 to right
print(d)

d1 = deque(range(5),5) #Max len of d1 is 5
print(d1)
d1.append(6)
print(d1)
d1.popleft()
print(d1)
d1.pop()
print(d1)