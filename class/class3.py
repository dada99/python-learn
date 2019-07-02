class Myclass3:
    name = "first"
    
    def __init__(self,age):
        self.age = age

myclass3_1 = Myclass3(10)
myclass3_2 = Myclass3(11)
print(myclass3_1.name)
print(myclass3_1.age)
Myclass3.name = "second"
print(myclass3_2.name)
print(myclass3_2.age)




