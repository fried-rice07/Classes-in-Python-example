class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return 'Name: ' + self.name +'\n' +'Age:' + self.age
class Student(Person):
    def __init__(self,name, age, section):
        Person.__init__(self, name, age)
        self.section = section
    def displayStudent(self):
        return 'StudentName: '+self.name+'\n' +'StudentAge: '+self.age+"\n" + "Section: " + self.section

person = Person('Marcel', '19')
print(person.display())
print('--------------')
student = Student('Marcel', '19', 'BSCPE 2A')
print(student.displayStudent())





