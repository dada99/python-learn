def func1():
    a = "1" #local variable of the function
    print(a)
a = "2" # global variable
print(a) # should be 2
func1() # should be 1
print(a) # still should be 2
print(func1)
func2 = func1
print(func2)
