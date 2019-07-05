import random
num_list = []
for i in range(10):
    num_list.append(random.randint(0,100)) # create a list with 10 random numbers
print(num_list)
for x in num_list:
    if(x <= 50):
       print("Hit the lower range")
    elif(x > 80):
       print("Hit the highest range")
    else:
        print("Hit the middle range")