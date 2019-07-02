class Myclass4:
    name = "first"    
    def __init__(self,age):
        self.age = age

class Submyclass4(Myclass4):
    pass

submyclass4_1 = Submyclass4(10)
print(submyclass4_1.name)
print(submyclass4_1.age)
print(isinstance(submyclass4_1,Myclass4))
print(issubclass(Submyclass4,Myclass4))



