class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "%s %s"%(self.name, self.age)
test = Student("Marcel",19)
print(test)

