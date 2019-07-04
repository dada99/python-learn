def just_a_exception(n):
    if n > 10:
        raise Exception('n should not execeed 10')
    print("It's valid number:"+str(n))
for i in range(9,12):
   just_a_exception(i)


    