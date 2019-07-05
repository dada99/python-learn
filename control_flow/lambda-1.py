lam = lambda x,y: (x+y)*2
print(lam(2,3))

high_ord_func = lambda x, func: x + func(x)# A lambda function can be a higher-order function by taking a function (normal or lambda) as an argument
high_ord_func(2, lambda x: x * x) #Python exposes higher-order functions as built-in functions or in the standard library. Examples include map(), filter(), functools.reduce(), as well as key functions like sort(), sorted(), min(), and max(). 




