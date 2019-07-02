class MyClass2:
    x = 1
    y = 2
    def func1(self):
        print(self.x)
    def changex(self,new_x):
        self.x = new_x

    
myclass2 = MyClass2()
myclass2.func1()
myclass2.changex(3)
print(myclass2.x)
