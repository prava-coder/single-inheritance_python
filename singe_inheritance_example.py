#base class/parent class
class operations():
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
#to add two values(value1,value2)
    def addition(self,value1,value2):
        print("to add value1 is:",self.value1)
        print("to add value2 is:",self.value2)
        return self.value1+self.value2
#to subract two values(value1,value2)
    def subraction(self,value1,value2):
        print("to subract value1 is:",self.value1)
        print("to subract value2 is:",self.value2)
        return self.value1-self.value2
#to multiply two values(value1,value2)
    def multiplication(self,value1,value2):
        print("to multiply value1 is:",self.value1)
        print("to multiply value2 is:",self.value2)
        return self.value1*self.value2
#creating another class(child class)
class caluclation(operations):
             pass

object1=caluclation(10,10)
print(object1.addition(10,10))
print("")
object2=caluclation(20,30)
print(object2.subraction(20,30))
print("")
object3=caluclation(40,40)
print(object3.multiplication(40,40))
print("")